var array = [];
angular.module('lncRNASNP2')
    .controller('LineController', LineController);

function LineController($scope, $http, lncRNASNP2Service, $routeParams,$window,$route) {
    var base_url = lncRNASNP2Service.getAPIBaseUrl();

    $scope.search_lncrna = $routeParams.lncrna;
    $scope.fetch_lncrna = function () {
        $http({
            url: base_url + '/api/lncrna_match_result',
            params: {lncrna: $routeParams.lncrna},
            method: 'GET'
        }).then(
            function (response) {
                var temp=response.data.match_result;
                if (temp.length==0){
                    $scope.error=1
                }
                if(temp.length==1){
                    if(temp[0]['lncrna']){
                        $window.open("#!/lncrna_info?lncrna="+temp[0]['lncrna'],"_self")
                    }else{
                        $window.open("#!/lncrna_info?lncrna="+temp[0]['transcript'],"_self")
                    }
                }
                if(temp.length>1){
                    if(temp[0]['lncrna']){
                        $scope.lnc = 1
                    }else{
                        $scope.alias = 1
                    }
                    $scope.lncrna_list = response.data.match_result;
                }
            }
        )
    };
    $scope.fetch_lncrna();
}