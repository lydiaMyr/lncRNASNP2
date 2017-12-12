'use strict';

angular.module('lncRNASNP2')
    .controller('MirnaDetailController', MirnaDetailController)
    .controller('TargetController',TargetController);

function MirnaDetailController($scope,$http,$routeParams,lncRNASNP2Service) {
    $scope.initial = 1;
    var snp_tag = $routeParams.snp;
    if (snp_tag==1){
        $scope.snp_tag=1
    }else{
        $scope.not_snp_tag=1
    }
    $scope.clear = function () {
        $scope.one=0;
        $scope.two=0;
        $scope.three=0;
    };
    var flag=0;
    $scope.one=1;
    $scope.show_one = function (refer) {
        $scope.clear();
        if (refer=="one"){
            $scope.one=1;
            $scope.class_one ="active"
        }
        if (refer=="two"){
            $scope.two=1;
            $scope.class_two ="active"
        }
        if (refer=="three"){
            $scope.three=1;
            $scope.class_three ="active"
        }
    };
    $("[data-toggle='popover']").popover();
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    $scope.check = function (query_item) {
        if(/[@#\$%\^&\*]+/g.test(query_item)){
            flag=1;
            alert("Invalid input");
            history.back();
        }
    };
    $scope.fetch_tcga_target_gain = function () {
        $http({
            url: base_url+'/api/tcga_target_gain_list',
            params: {"miRNA":$routeParams.mirna},
            method: 'GET'
        }).then(
            function(response){
                var temp = response.data.target_gain_list;
                $scope.tcga_gain_count=temp.length;
                $scope.tcga_target_gain = response.data.target_gain_list
            }
        )
    };
    $scope.fetch_tcga_target_loss = function () {
        $http({
            url: base_url+'/api/tcga_target_loss_list',
            params: {"miRNA":$routeParams.mirna},
            method: 'GET'
        }).then(
            function(response){
                var temp = response.data.target_loss_list;
                $scope.tcga_loss_count=temp.length;
                $scope.tcga_target_loss = response.data.target_loss_list
            }
        )
    };
    $scope.fetch_cosmic_target_gain = function () {
        $http({
            url: base_url+'/api/cosmic_target_gain_list',
            params: {"miRNA":$routeParams.mirna},
            method: 'GET'
        }).then(
            function(response){
                var temp = response.data.target_gain_list;
                $scope.cosmic_gain_count=temp.length;
                $scope.cosmic_target_gain = response.data.target_gain_list
            }
        )
    };
    $scope.fetch_cosmic_target_loss = function () {
        $http({
            url: base_url+'/api/cosmic_target_loss_list',
            params: {"miRNA":$routeParams.mirna},
            method: 'GET'
        }).then(
            function(response){
                var temp = response.data.target_loss_list;
                $scope.cosmic_loss_count=temp.length;
                $scope.cosmic_target_loss = response.data.target_loss_list
            }
        )
    };

    $scope.mirna_info = function () {
        $http({
            url: base_url+'/api/miR_basic_list',
            params: {mirna:$routeParams.mirna,single_tag:1},
            method: 'GET'
        }).then(
            function success(response) {
                var temp;
                temp = response.data.miR_basic_list;
                if (temp.length>0){
                    $scope.miRNA = temp[0];
                }else{
                    $scope.error=1
                }
            },
            function error(response) {
                console.log("wrong");
            }
        )
    };
    $scope.mirna_info();
    $scope.fetch_target_gain = function () {
        $http({
            url: base_url+'/api/target_gain_list',
            params: {miRNA:$routeParams.mirna},
            method: 'GET'
        }).then(
            function(response){
                var temp = response.data.target_gain_list;
                $scope.initial = 0;
                if (temp.length>0){
                    $scope.gain = 1
                }
                $scope.target_gain = temp;
                $scope.records_number_gain = response.data.records_gain;
            }
        )
    };
    $scope.search_mirna_gain = function () {
        var lncrna = $('#search_gain').val();
        $scope.check(lncrna);
        if(flag==0){
            $http({
                url: base_url+'/api/target_gain_list',
                params: {miRNA:$routeParams.mirna,lncrna:lncrna},
                method: 'GET'
            }).then(
                function(response){
                    var temp = response.data.target_gain_list;
                    if(temp.length==0){
                        $scope.gain_zero=1
                    }
                    $scope.records_number_gain = 0;
                    $scope.target_gain = response.data.target_gain_list;
                }
            )
        }
    };
    $scope.search_mirna_loss = function () {
        var lncrna = $('#search_loss').val();
        $scope.check(lncrna);
        if(flag==0){
            $http({
                url: base_url+'/api/target_loss_list',
                params: {miRNA:$routeParams.mirna,lncrna:lncrna},
                method: 'GET'
            }).then(
                function(response){
                    // console.log("hello world");
                    var temp = response.data.target_loss_list;
                    // console.log(temp.length);
                    if(temp.length==0){
                        $scope.loss_zero=1;
                    }
                    $scope.target_loss = response.data.target_loss_list;
                    $scope.records_number_loss=0

                }
            )
        }
    };
    // $scope.search_mirna_cons = function () {
    //     var lncrna = $('#cons').val();
    //     $http({
    //         url: base_url+'/api/mirna_target_list',
    //         params: {mirna:$routeParams.mirna,lncrna:lncrna,},
    //         method: 'GET'
    //     }).then(
    //         function(response){
    //             $scope.cons_mirna_target = response.data.cons_target_ls;
    //             $scope.cons_records_number = response.data.cons_records_number;
    //         }
    //     )
    // };
    $scope.search_mirna_non_cons = function () {
        var lncrna = $('#non_cons').val();
        $scope.check(lncrna);
        if(flag==0){
            $http({
                url: base_url+'/api/mirna_target_list',
                params: {mirna:$routeParams.mirna,lncrna:lncrna},
                method: 'GET'
            }).then(
                function(response){
                    // $scope.non_cons_records_number = response.data.non_cons_records_number;
                    var temp=response.data.non_cons_target_ls;
                    if(temp.length==0){
                        $scope.non_cons_zero=1;
                    }
                    $scope.non_cons_mirna_target = response.data.non_cons_target_ls;
                    $scope.non_cons_records_number = 0
                }
            )
        }

    };
    $scope.fetch_mirna_profile = function () {
        $http({
            url: base_url+'/api/mir_profile_list',
            params: {mirna:$routeParams.mirna},
            method: 'GET'
        }).then(
            function(response){
                var temp;
                var value;
                var array=[];
                var r,g,b;
                temp = response.data.mirna_profile;
                for (var key in temp[0]) {
                    if (temp[0][key]>500){
                        value=500
                    }else{
                        value = temp[0][key]
                    }
                    value=value/500*100-1;

                    if(value<50){
                        r = Math.floor(255*(value/50));
                        g = 255
                    }else{
                        r = 255;
                        g = Math.floor(255*((50-value%50)/50))
                    }
                    b = 0;
                    var p = "rgb("+r+","+g+","+b+")";
                    if ((temp[0][key])&&(key!="miR")){
                        array.push({"sample":key,"expression":temp[0][key],"color":p})
                    }
                }
                $scope.mirna_profile = array;
            }
        )
    };
    $scope.fetch_mirna_profile();
    $scope.fetch_target_loss = function () {
        $http({
            url: base_url+'/api/target_loss_list',
            params: {miRNA:$routeParams.mirna},
            method: 'GET'
        }).then(
            function(response){
                var temp = response.data.target_loss_list;
                if (temp.length>0){
                    $scope.loss = 1
                }
                $scope.target_loss = temp;
                $scope.records_number_loss = response.data.records_loss
            }
        )
    };
    $scope.update_page_loss = function (test,page,size,total) {
        $http({
            url: base_url+'/api/target_loss_list',
            params: {page:page,miRNA:$routeParams.mirna},
            method: 'GET'
        }).then(
            function(response){
                $scope.target_loss = response.data.target_loss_list;
            }
        )
    };
    $scope.fetch_target = function () {
        $http({
            url: base_url+'/api/mirna_target_list',
            params: {mirna:$routeParams.mirna},
            method: 'GET'
        }).then(
            function(response){
                var temp1 = response.data.cons_target_ls;
                var temp2 = response.data.non_cons_target_ls;
                $scope.initial = 0;
                if (temp1.length>0){
                    $scope.cons = 1
                }
                if (temp2.length>0){
                    $scope.non_cons = 1
                }
                $scope.cons_mirna_target = response.data.cons_target_ls;
                $scope.cons_records_number = response.data.cons_records_number;
                $scope.non_cons_records_number = response.data.non_cons_records_number;
                $scope.non_cons_mirna_target = response.data.non_cons_target_ls;
            }
        )
    };
    $scope.update_page_cons = function (test,page,size,total) {
        $http({
            url: base_url+'/api/mirna_target_list',
            params: {mirna:$routeParams.mirna,cons_page:page},
            method: 'GET'
        }).then(
            function(response){
                $scope.cons_mirna_target = response.data.cons_target_ls;
            }
        )
    };
    $scope.update_page_non_cons = function (test,page,size,total) {
        $http({
            url: base_url+'/api/mirna_target_list',
            params: {mirna:$routeParams.mirna,non_cons_page:page},
            method: 'GET'
        }).then(
            function(response){
                $scope.non_cons_mirna_target = response.data.non_cons_target_ls;
            }
        )
    };

    if (snp_tag==1){
        $scope.fetch_target_gain();
         $scope.fetch_target_loss();
        $scope.fetch_tcga_target_gain();
        $scope.fetch_tcga_target_loss();
        $scope.fetch_cosmic_target_gain();
        $scope.fetch_cosmic_target_loss();
    }
    if(snp_tag==0){
        $scope.fetch_target()
    }
}
function TargetController($scope,$http,$routeParams,lncRNASNP2Service) {
    var base_url = lncRNASNP2Service.getAPIBaseUrl();
    $scope.mirna = $routeParams.mirna;
    $scope.lncrna = $routeParams.lncrna;
    $scope.fetch_target = function () {
        $http({
            url: base_url + '/api/mirna_target_list',
            params: {mirna: $routeParams.mirna,lncrna:$routeParams.lncrna,t_start:$routeParams.start},
            method: 'GET'
        }).then(
            function (response) {
                var temp = response.data.target;
                $scope.target = temp[0]
            }
        )
    };
    $scope.fetch_target()
}
