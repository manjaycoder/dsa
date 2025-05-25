/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var binary=(nums,target,isSerach)=>{
     let start=0;
    let end=nums.length-1
    let ans=-1
    while(start<=end){
        let mid=Math.floor((start+end)/2)
        if(nums[mid]===target){
            ans=mid
            if(isSerach){
                end=mid-1
            }else{
                start=mid+1
           
        }}else if(nums[mid]<target)
            start=mid+1
        else
            end=mid-1
        
        
    }
    return ans


}
var searchRange = function(nums, target) {
   let start=binary(nums,target,true)
let end=binary(nums,target,false)
return  [start,end]



};