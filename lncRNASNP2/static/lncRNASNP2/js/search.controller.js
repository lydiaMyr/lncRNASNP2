'use strict';

angular.module('lncRNASNP2')
    .controller('SearchController', SearchController);

function SearchController($scope,lncRNASNP2Service,$routeParams,$http) {
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    $("[data-toggle='popover']").popover();
    $scope.fetch_snp_batch = function (query_ls) {
        $http({
            url: base_url+'/api/lncrna_snp_list',
            params: {'snp':query_ls},
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                $scope.lncrna_snp_list = response.data.lncrna_snp_list;
            },
            function error(response) {
                $scope.snp=0;
                $scope.error = 1
            }
        )
    };
    $scope.fetch_snp = function () {
        $http({
            url: base_url+'/api/lncrna_snp_list',
            params:{chr:$routeParams.chromosome,start:Number($routeParams.start),end:Number($routeParams.end)},
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                $scope.records_number = response.data.records_number;
                $scope.lncrna_snp_list = response.data.lncrna_snp_list;
            },
            function error(response) {
                $scope.ld=0;
                $scope.error=1
            }
        )
    };
    $scope.fetch_lncrna_batch = function (query_ls) {
        $http({
            url: base_url+'/api/lncrna_gene_list',
            params: {'lncrna':query_ls},
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                $scope.lncrna_gene_list = response.data.lncrna_gene_list;
            },
            function error(response) {
                $scope.lncrna = 0;
                $scope.error=1
            }
        )
    };
    $scope.mirna_info = function (query_ls) {
        $http({
            url: base_url+'/api/miR_basic_list',
            params: {mirna:query_ls},
            method: 'GET'
        }).then(
            function success(response) {
                console.log(response);
                $scope.mirna_file = response.data.miR_basic_list;
            },
            function error(response) {
                $scope.mirna = 0;
                $scope.error = 1
            }
        )
    };
    if($routeParams.chromosome){
        console.log('query_ld');
        $scope.ld=1;
        $scope.chr =$routeParams.chromosome;
        $scope.start = $routeParams.start;
        $scope.end = $routeParams.end;
        $scope.fetch_snp();
    }
    if($routeParams.snp){
        $scope.snp = 1;
        var query = $routeParams.snp;
        $scope.fetch_snp_batch(query)
    }
    if($routeParams.mirna){
        $scope.mirna = 1;
        var query = $routeParams.mirna;
        $scope.mirna_info(query)
    }
    if($routeParams.lncrna){
        $scope.lncrna = 1;
        var query = $routeParams.lncrna;
        $scope.fetch_lncrna_batch(query)
    }
    $scope.update_page = function (test,page,size,total) {
        console.log("hello");
        var condition={};
        condition['page'] = page;
        condition['chr'] = $routeParams.chrmosome;
        condition['start'] = Number($routeParams.start);
        condition['end'] = Number($routeParams.end);
        $http({
            url: base_url+'/api/lncrna_snp_list',
            params: condition,
            method: 'GET'
        }).then(
            function (response) {
                $scope.lncrna_snp_list = response.data.lncrna_snp_list;
            }
        )
    };
}


