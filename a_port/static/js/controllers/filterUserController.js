/**
 * Created by GoldenGate on 11/10/14.
 */
function filterUserController($scope, $http, $routeParams) {
    var first = $routeParams.name;
    $scope.first = first
    console.log(first);
    $http.get('/api/users/?first_name='+first).
        success(function(data){
            $scope.users = data.results;
            console.log(data.results)
        }).error(function(error) {
            console.log("didn't work");
            console.log(error);
        });
}