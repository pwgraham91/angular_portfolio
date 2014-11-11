/**
 * Created by GoldenGate on 11/10/14.
 */
function filterUserController($scope, $http, $routeParams) {
    var first = $routeParams.name;
    console.log(first);
    $http.get('/users/?first_name='+first).
        success(function(data){
            $scope.users = data;
            console.log(data)
        }).error(function(error) {
            console.log("didn't work");
            console.log(error);
        });
}