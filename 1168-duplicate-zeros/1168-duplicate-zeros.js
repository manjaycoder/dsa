/**
 * @param {number[]} arr
 * @return {void} Do not return anything, modify arr in-place instead.
 */
var duplicateZeros = function(arr) {
    let zero=0;
    for(let i=0;i<arr.length;i++){
        if(arr[i] ==0){
zero++;
        }
    }

    let i=arr.length-1;
    let j=(arr.length-1)+zero;
    while(i != j){
        if(j<arr.length){
            arr[j]=arr[i];
        }
        j--;
        if(arr[i]==0){
            if(j<arr.length){
                arr[j]=arr[i];
            }
            j--;
        }
        i--;
    }

};