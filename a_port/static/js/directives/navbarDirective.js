/**
 * Created by GoldenGate on 11/11/14.
 */
a_port.directive('navbarA', function(){
    return {
        restrict: "E",
        templateUrl: "/static/js/directives/templates/navbar.html",
        replace: "true",
        controller: function ($scope, $location) {

        }
    }
});