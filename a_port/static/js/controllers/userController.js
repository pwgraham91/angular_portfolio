/**
 * Created by GoldenGate on 11/10/14.
 */
function userController($scope, $http, $routeParams) {
    var userId = $routeParams.id;
    $http.get('http://127.0.0.1:8000/users/'+userId+'/.json').
        success(function (data) {
            $scope.user = data;
            console.log(data)
        }).error(function (error) {
            console.log("didn't work");
            console.log(error);
        });
}