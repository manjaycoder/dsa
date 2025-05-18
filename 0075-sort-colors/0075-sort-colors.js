/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let zero = 0, one = 0, two = 0;

    for (let n of nums) {
        if (n === 0) zero++;
        else if (n === 1) one++;
        else two++;
    }

    for (let i = 0; i < nums.length; i++) {
        if (zero > 0) {
            nums[i] = 0;
            zero--;
        } else if (one > 0) {
            nums[i] = 1;
            one--;
        } else {
            nums[i] = 2;
            two--;
        }
    }
};