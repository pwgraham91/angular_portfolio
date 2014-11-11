/**
 * Created by GoldenGate on 11/4/14.
 */
function homeController($scope, $http) {
    $scope.count = 10;
    $http.get('/users/.json').
        success(function(data){
            $scope.users = data.results;
            console.log(data)
        }).error(function(error) {
            console.log("didn't work");
            console.log(error);
        });
    $http.get('/projects/.json').
        success(function(data){
            $scope.projects = data.results;
            $scope.count = data.count;
            console.log($scope.count);
            console.log(data)
        }).error(function(error) {
            console.log("didn't work");
            console.log(error);
        });
//    workaround for the bootstrap. real amount of items + 10
$scope.totalItems = $scope.count + 10;
$scope.currentPage = 1;
$scope.setPage = function (pageNo) {
$scope.currentPage = pageNo;
  };
$scope.pageChanged = function() {
    console.log('Page changed to: ' + $scope.currentPage);
                  $http.get('/projects/.json?page='+$scope.currentPage).
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