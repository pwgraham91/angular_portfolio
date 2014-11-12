/**
 * Created by GoldenGate on 11/10/14.
 */
function userController($scope, $http, $routeParams) {
    $scope.count = 10;
    var userId = $routeParams.id;
    $http.get('/api/users/'+userId+'/.json').
        success(function (data) {
            $scope.user = data;
            console.log(data)
        }).error(function (error) {
            console.log("didn't work");
            console.log(error);
        });
    $http.get('/api/projects/?owner__id='+userId).
        success(function (data) {
            $scope.projects = data.results;
            console.log(data)
        }).error(function (error) {
            console.log("didn't work");
            console.log(error);
        });
    $scope.totalItems = $scope.count + 10;
    $scope.currentPage = 1;
    $scope.setPage = function (pageNo) {
    $scope.currentPage = pageNo;
      };
    $scope.pageChanged = function() {
        console.log('Page changed to: ' + $scope.currentPage);
                      $http.get('/api/projects/?owner__id=1&page='+$scope.currentPage).
                success(function(data){
                    $scope.projects = data.results;
                })
                .error(function(error) {
                    console.log("didn't work");
                    console.log(error);
                });
      };
    // pagination size
    $scope.maxSize = 5;
    $scope.bigTotalItems = 175;
    $scope.bigCurrentPage = 1;
}