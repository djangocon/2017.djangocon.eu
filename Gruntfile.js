module.exports = function (grunt) {

    var mozjpeg = require('imagemin-mozjpeg');

    grunt.initConfig({

        pkg: grunt.file.readJSON('package.json'),

        paths: {
            'css': './static/css/',
            'images': './static/img/',
            'js': './apps/',
            'media': './tmp/media/',
            'sass': './styles/',
            'assets_images': './assets/img/'
        },

        patterns: {
            'images': [
                '<%= paths.images %>*',
                '<%= paths.images %>**/*'
            ],
            'js': [
                '<%= paths.js %>*.js',
                '<%= paths.js %>**/*.js',
                '!<%= paths.js %>*.min.js',
                '!<%= paths.js %>**/*.min.js',
            ],
            'media': ['<%= paths.media %>**/*'],
            'sass': [
                '<%= paths.sass %>*.scss',
                '<%= paths.sass %>**/*.scss'
            ],
            'assets_images': [
                '<%= paths.assets_images %>*.{png,jpg,jpeg,gif}',
                '<%= paths.assets_images %>**/*.{png,jpg,jpeg,gif}'
            ]
        },

        jshint: {
            files: "<%= patterns.js %>",
            options: {
                jshintrc: ".jshintrc"
            }
        },

        compass: {
            compile: {
                options: {
                    sassDir: '<%= paths.sass %>',
                    cssDir: '<%= paths.css %>',
                    outputStyle: 'compressed'
                }
            }
        },

        scsslint: {
            allFiles: '<%= patterns.sass %>',
            options: {
                config: '.scss-lint.yml',
                colorizeOutput: true,
                config: null
            },
        },

        imagemin: {
            static: {
                options: {
                    optimizationLevel: 3,
                    svgoPlugins: [{ removeViewBox: false }],
                    use: [mozjpeg()]
                },
                files: [{
                    expand: true,
                    src: '<%= patterns.assets_images %>',
                    dest: '<%= paths.images %>'
                }]
            },
        },

        watch: {
            css: {
                files: '<%= patterns.sass %>',
                tasks: ['scsslint', 'compass'],
                options: {
                    livereload: true,
                },
            },
        },

    });

    for (var key in grunt.file.readJSON('package.json').devDependencies) {
        if (key !== 'grunt' && key.indexOf('grunt') === 0) {
            grunt.loadNpmTasks(key);
        }
    }

    grunt.registerTask('compile', ['scsslint', 'compass', 'imagemin']);
    grunt.registerTask('ci', ['scsslint']);
    grunt.registerTask('default', ['watch']);
};
