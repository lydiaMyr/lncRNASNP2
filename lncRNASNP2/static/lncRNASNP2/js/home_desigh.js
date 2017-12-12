/**
 * Created by Administrator on 2017/6/16.
 */
angular.module('lncRNASNP2')
    .controller('HomeTestController', HomeTestController);

function HomeTestController($scope,$http,$window,$routeParams,lncRNASNP2Service) {



    var eleBack = null, eleFront = null,
    // 纸牌元素们
    eleList = $(".list");

// 确定前面与后面元素
    $scope.funBackOrFront = function() {
    eleList.each(function() {
        if ($(this).hasClass("out")) {
            eleBack = $(this);
        } else {
            eleFront = $(this);
        }
    });
};
$scope.funBackOrFront();


$("#box").bind("click", function() {
    // 切换的顺序如下
    // 1. 当前在前显示的元素翻转90度隐藏, 动画时间225毫秒
    // 2. 结束后，之前显示在后面的元素逆向90度翻转显示在前
    // 3. 完成翻面效果
    eleFront.addClass("out").removeClass("in");
    setTimeout(function() {
        eleBack.addClass("in").removeClass("out");
        // 重新确定正反元素
        funBackOrFront();
    }, 225);
    return false;
});
}
