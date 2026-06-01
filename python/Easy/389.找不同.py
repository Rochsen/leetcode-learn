"""
389. 找不同

给你两个字符串 s 和 t，它们只包含小写字母。

字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。

请找出在 t 中被添加的字母。
"""


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        :param s: str
        :param t: str
        :return: str
        """
        # C 语言实现方法启发
        m = s+t
        sum_s, sum_t = 0, 0

        for i in s:
            sum_s += ord(i)
        
        for u in t:
            sum_t += ord(u)

        return chr(sum_t - sum_s)
    
        # for i in t:  # 遍历字符串 t 中的每个字符
        #     if t.count(i) != s.count(i):  # 如果 t 中该字符的个数和 s 中该字符的个数不相等
        #         return i  # 返回该字符
        
        # s += "?"
        # for i, j in zip(t, s):
        #     if i != j:
        #         return i

        
        # 方法1：使用计数
        # from collections import Counter
        # count_s = Counter(s)
        # count_t = Counter(t)
        # for char, count in count_t.items():
        #     if count_s.get(char, 0) != count:
        #         return char
        
        # 方法2：使用异或运算（更高效）
        # result = 0
        # for c in s + t:
        #     result ^= ord(c)
        # return chr(result)


if __name__ == '__main__':
    # 测试用例1：添加的字符在末尾
    s = "a"
    t = "aa"
    print("测试用例1:", Solution().findTheDifference(s, t))  # 应输出 'a'
    
    # 测试用例2：添加的字符在中间
    s = "abcd"
    t = "abcde"
    print("测试用例2:", Solution().findTheDifference(s, t))  # 应输出 'e'
    
    # 测试用例3：添加的字符是重复的
    s = "xyz"
    t = "xyzz"
    print("测试用例3:", Solution().findTheDifference(s, t))  # 应输出 'z'

    s = "ymbgaraibkfmvocpizdydugvalagaivdbfsfbepeyccqfepzvtpyxtbadkhmwmoswrcxnargtlswqemafandgkmydtimuzvjwxvlfwlhvkrgcsithaqlcvrihrwqkpjdhgfgreqoxzfvhjzojhghfwbvpfzectwwhexthbsndovxejsntmjihchaotbgcysfdaojkjldprwyrnischrgmtvjcorypvopfmegizfkvudubnejzfqffvgdoxohuinkyygbdzmshvyqyhsozwvlhevfepdvafgkqpkmcsikfyxczcovrmwqxxbnhfzcjjcpgzjjfateajnnvlbwhyppdleahgaypxidkpwmfqwqyofwdqgxhjaxvyrzupfwesmxbjszolgwqvfiozofncbohduqgiswuiyddmwlwubetyaummenkdfptjczxemryuotrrymrfdxtrebpbjtpnuhsbnovhectpjhfhahbqrfbyxggobsweefcwxpqsspyssrmdhuelkkvyjxswjwofngpwfxvknkjviiavorwyfzlnktmfwxkvwkrwdcxjfzikdyswsuxegmhtnxjraqrdchaauazfhtklxsksbhwgjphgbasfnlwqwukprgvihntsyymdrfovaszjywuqygpvjtvlsvvqbvzsmgweiayhlubnbsitvfxawhfmfiatxvqrcwjshvovxknnxnyyfexqycrlyksderlqarqhkxyaqwlwoqcribumrqjtelhwdvaiysgjlvksrfvjlcaiwrirtkkxbwgicyhvakxgdjwnwmubkiazdjkfmotglclqndqjxethoutvjchjbkoasnnfbgrnycucfpeovruguzumgmgddqwjgdvaujhyqsqtoexmnfuluaqbxoofvotvfoiexbnprrxptchmlctzgqtkivsilwgwgvpidpvasurraqfkcmxhdapjrlrnkbklwkrvoaziznlpor"
    t = "qhxepbshlrhoecdaodgpousbzfcqjxulatciapuftffahhlmxbufgjuxstfjvljybfxnenlacmjqoymvamphpxnolwijwcecgwbcjhgdybfffwoygikvoecdggplfohemfypxfsvdrseyhmvkoovxhdvoavsqqbrsqrkqhbtmgwaurgisloqjixfwfvwtszcxwktkwesaxsmhsvlitegrlzkvfqoiiwxbzskzoewbkxtphapavbyvhzvgrrfriddnsrftfowhdanvhjvurhljmpxvpddxmzfgwwpkjrfgqptrmumoemhfpojnxzwlrxkcafvbhlwrapubhveattfifsmiounhqusvhywnxhwrgamgnesxmzliyzisqrwvkiyderyotxhwspqrrkeczjysfujvovsfcfouykcqyjoobfdgnlswfzjmyucaxuaslzwfnetekymrwbvponiaojdqnbmboldvvitamntwnyaeppjaohwkrisrlrgwcjqqgxeqerjrbapfzurcwxhcwzugcgnirkkrxdthtbmdqgvqxilllrsbwjhwqszrjtzyetwubdrlyakzxcveufvhqugyawvkivwonvmrgnchkzdysngqdibhkyboyftxcvvjoggecjsajbuqkjjxfvynrjsnvtfvgpgveycxidhhfauvjovmnbqgoxsafknluyimkczykwdgvqwlvvgdmufxdypwnajkncoynqticfetcdafvtqszuwfmrdggifokwmkgzuxnhncmnsstffqpqbplypapctctfhqpihavligbrutxmmygiyaklqtakdidvnvrjfteazeqmbgklrgrorudayokxptswwkcircwuhcavhdparjfkjypkyxhbgwxbkvpvrtzjaetahmxevmkhdfyidhrdeejapfbafwmdqjqszwnwzgclitdhlnkaiyldwkwwzvhyorgbysyjbxsspnjdewjxbhpsvj"
    print("测试用例4:", Solution().findTheDifference(s, t))  # 应输出 't'
    