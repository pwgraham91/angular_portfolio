var a_port = angular.module('a_port', ['ngRoute', 'ngResource', 'ngSanitize', 'ui.bootstrap']);
a_port.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {templateUrl: '/static/js/views/home.html', controller: homeController}).
        when('/user/:id', {templateUrl: '/static/js/views/user.html', controller: userController}).
        when('/filterUser/:name', {templateUrl: '/static/js/views/filterUser.html', controller: filterUserController}).
        otherwise({redirectTo: '/'});
}]);
