/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    private TreeNode result;
    private int maxDepth = 0;
    public TreeNode lcaDeepestLeaves(TreeNode root) {
        dfs(root, 0);
        return result;
    }

    int dfs(TreeNode node, int depth) {
        if (node == null) {
            maxDepth = Math.max(maxDepth, depth);
            return depth;
        }
        int leftDepth = dfs(node.left, depth + 1);
        int rightDepth = dfs(node.right, depth + 1);
        if (leftDepth == maxDepth && rightDepth == maxDepth) {
            result = node;
        }
        return Math.max(leftDepth, rightDepth);
    }
}