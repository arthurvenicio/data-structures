/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  var map = new Map();

  for (let i = 0; i <= nums.length; i++) {
    let diff = target - nums[i];

    if (map.has(diff)) {
      return [map.get(diff), i];
    }

    if (!map.has(nums[i])) {
      map.set(nums[i], i);
    }
  }
};