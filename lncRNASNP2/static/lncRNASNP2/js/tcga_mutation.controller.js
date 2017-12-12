'use strict';

angular.module('lncRNASNP2')
    .controller('TcgaMutationController', TcgaMutationController);
function TcgaMutationController($scope,$http,$routeParams,lncRNASNP2Service) {
    console.log("TcgaMutationController loaded");
    var cancer = $routeParams.cancer;
    $scope.initial = 1;
    $scope.cancer_type = $routeParams.cancer;
    $("[data-toggle='popover']").popover();
    $scope.page_cancer = cancer;
    $scope.click_tree = 1;
    var flag = 0;
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    $scope.check = function (query_item) {
        if (/[@#\$%\^&\*]+/g.test(query_item)) {
            flag = 1;
            alert("Invalid input");
            history.back();
        }
    };


    $scope.currentPage = $routeParams.page;
    $scope.fetch_tcga_list = function (cancer_type) {
        $http({
            url: base_url + '/api/tcga_lnc_list',
            params: {cancer: cancer_type},
            method: 'GET'
        }).then(
            function (response) {
                $scope.tcga_lnc_list = response.data.TCGA_lnc_list;
                $scope.tanric = response.data.tanric;
                $scope.records_number = response.data.records_number;
            }
        )
    };

    $scope.fetch_tcga_list(cancer);
    $scope.update_page = function (page_cancer, page, size, total) {
        $http({
            url: base_url + '/api/tcga_lnc_list',
            params: {page: page, cancer: $scope.page_cancer},
            method: 'GET'
        }).then(
            function (response) {
                console.log(response);
                $scope.tcga_lnc_list = response.data.TCGA_lnc_list;
            }
        )
    };
    $scope.show_mutaion_detail = function () {
        window.opne("#!")

    };
    $scope.roleList1 = [
        {
            roleName: "TCGA Cancer Types", roleId: "all", children: [
            {roleName: "ACC", roleId: "acc", children: []},
            {roleName: "BLCA", roleId: "blca", children: []},
            {roleName: "BRCA", roleId: "brca", children: []},
            {roleName: "CESC", roleId: "cesc", children: []},
            {roleName: "CHOL", roleId: "chol", children: []},
            {roleName: "COAD", roleId: "coad", children: []},
            {roleName: "DLBC", roleId: "dlbc", children: []},
            {roleName: "ESCA", roleId: "esca", children: []},
            {roleName: "GBM", roleId: "gbm", children: []},
            {roleName: "HNSC", roleId: "hnsc", children: []},
            {roleName: "KICH", roleId: "kich", children: []},
            {roleName: "KIRC", roleId: "kirc", children: []},
            {roleName: "KIRP", roleId: "kirp", children: []},
            {roleName: "LAML", roleId: "laml", children: []},
            {roleName: "LGG", roleId: "lgg", children: []},
            {roleName: "LIHC", roleId: "lihc", children: []},
            {roleName: "LUAD", roleId: "luad", children: []},
            {roleName: "LUSC", roleId: "lusc", children: []},
            {roleName: "OV", roleId: "ov", children: []},
            {roleName: "PAAD", roleId: "paad", children: []},
            {roleName: "PCPG", roleId: "pcpg", children: []},
            {roleName: "PRAD", roleId: "prad", children: []},
            {roleName: "READ", roleId: "read", children: []},
            {roleName: "SARC", roleId: "sarc", children: []},
            {roleName: "SKCM", roleId: "skcm", children: []},
            {roleName: "STAD", roleId: "stad", children: []},
            {roleName: "TGCT", roleId: "tgct", children: []},
            {roleName: "THCA", roleId: "thca", children: []},
            {roleName: "THYM", roleId: "thym", children: []},
            {roleName: "UCEC", roleId: "ucec", children: []},
            {roleName: "UCS", roleId: "ucs", children: []},
            {roleName: "UVM", roleId: "uvm", children: []}
        ]
        }];
    $scope.$watch('mytree.currentNode', function () {
        if ($scope.mytree && angular.isObject($scope.mytree.currentNode)) {
            cancer = $scope.mytree.currentNode.roleName;
            $scope.page_cancer = cancer;
            $scope.click_tree = 0
        }
        $scope.fetch_tcga_list(cancer)
    });
    $scope.search_query = function () {
        console.log($scope.page_cancer);
        $scope.initial = 0;
        var lnc = $('#search').val();
        //console.log(lnc);
        $scope.check(lnc);
        if (flag == 0) {
            $http({
                url: base_url + '/api/tcga_lnc_list',
                params: {cancer: $scope.page_cancer, lncrna: lnc, query: 1},
                method: 'GET'
            }).then(
                function (response) {
                    var temp = response.data.TCGA_lnc_list;
                    if (temp.length == 0) {
                        $scope.error = 1
                    }
                    $scope.tcga_lnc_list = response.data.TCGA_lnc_list;
                    $scope.tanric = response.data.tanric;
                    $scope.records_number = response.data.records_number;
                }
            )

        }
    };
}



