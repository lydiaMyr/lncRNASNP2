'use strict';
angular.module('lncRNASNP2')
    .controller('TestController', TestController)
    .controller('TestPageController', TestPageController);

function  TestPageController($scope,$http,$routeParams,lncRNASNP2Service) {
    console.log("TestPageController loaded");
    var structure_array = [];
    $scope.currentPage = $routeParams.page;
    $scope.fetch_lncrna_snp_list = function () {
        $http({
            url: '/api/ensembl',
            params: {ensembl: $routeParams.lncrna},
            method: 'GET'
        }).then(
            function (response) {
                var sum = 0;
                console.log(response);
                var trans_ls = response.data.ensembl_list;
                console.log(trans_ls);
                if (trans_ls.length == 1) {
                    var start = Number(trans_ls[0]['start']);
                    var end = Number(trans_ls[0]['end']);
                    sum = end - start;
                    structure_array.push({"start": 0, "end": end - start})
                } else {
                    var start = Number(trans_ls[0]['start']);
                    sum = 0;
                    for (var i = 0; i < trans_ls.length; i++) {
                        var start_exon = Number(trans_ls[i]['start']) - start;
                        var end_exon = Number(trans_ls[i]['end']) - start;
                        structure_array.push({"start": start_exon, "end": end_exon});
                        sum += end_exon - start_exon + 50 * i
                    }
                }
                $scope.line_width = sum
            }
        )
    };
    $scope.fetch_lncrna_snp_list();
    $scope.fetch_mre = function () {
        var mre_array = [];
        $http({
            url: '/api/mre',
            params: {ensembl: $routeParams.lncrna},
            method: 'GET'
        }).then(
            function (response) {
                var mre_list = response.data.mre_list;
                for (var i = 0; i < mre_list.length; i++) {
                    var mirna = mre_list[i]['miRNAs'];
                    var kmer = mre_list[i]['Kmer'];
                    var position = mre_list[i]['Positions'].split(',');
                    mre_array.push({"miRNA": mirna, "position": position, "kmer": kmer,"y_lable":70+i*20})
                }
                console.log(mre_array);
                $scope.mre_array = mre_array
            })
    };
    $scope.fetch_mre()
}

function TestController($scope, $http, lncRNASNP2Service, $routeParams,$window,$route) {
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    console.log("TestController loaded");
    $scope.search_mirna = $routeParams.mirna;
    $scope.fetch_mirna = function () {
        $http({
            url: base_url + '/api/match_result',
            params: {mirna:$routeParams.mirna},
            method: 'GET'
        }).then(
            function (response) {
                var temp = response.data.match_result;
                if (temp.length==0){
                    $scope.error=1
                }
                if(temp.length==1){
                    $window.open("#!/mirna_info?mirna="+temp[0]['mirna'],"_self")
                }
                if(temp.length>1){
                    $scope.mir_list = response.data.match_result;
                }
            }
        )
    };
    $scope.fetch_mirna();

    $scope.fetch_lncrna = function () {
        $http({
            url: base_url + '/api/mre',
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                $scope.records_number = response.data.records_num;
                $scope.mre_list = response.data.mre_list;
            }
        )
    };
    $scope.fetch_lncrna();
    $scope.show_structure = function (trans) {
        var name = trans["TransID"];
        window.open(base_url + "#!/mre_graph?lncrna=" + name, "_self")
    };

    $scope.update_page = function (test, page, size, total) {
        $http({
            url: base_url + '/api/mre',
            params: {page: page},
            method: 'GET'
        }).then(
            function (response) {
                $scope.mre_list = response.data.mre_list;
            }
        )
    }
}