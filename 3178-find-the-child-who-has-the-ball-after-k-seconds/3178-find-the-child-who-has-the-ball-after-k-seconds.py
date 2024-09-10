class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        # # modulo, children list 를 만든 다음, 뒤집어서 한번 붙이기
        # children = [x for x in range(n)]
        # queue = children + children[1:-1][::-1]

        # return 0

        cycle_length = 2 * (n - 1)
        
        k = k % cycle_length
        
        if k < n:
            return k
        else:
            return 2 * (n - 1) - k
