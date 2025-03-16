from typing import List,Tuple
'''
编程语言管理系统
'''


class CodeStatsSystem:
    # 初始化产品及其代码仓关系，所有代码仓的代码量为0
    # products[i] =[product_id，repoIDs[]] 表示一个产品，和它的代码仓列表
    # 产品，代码仓全局唯一，一个代码仓属于一个产品，一个代码仓里面有多种语言
    def __init__(self,products:List[Tuple[int,List[int]]]):
        self.products = {}  # {10: {102: [], 101: []}, 12: {122: []}, 22: {221: []}}
        self.map = {} # {102: 10, 101: 10, 122: 12, 221: 22}
        for product in products:
            product_id = product[0]
            repoIDs = product[1]
            repo = {}
            for repoID in repoIDs:
                repo[repoID] = repo.get(repoID, {})
                self.map[repoID] = product_id
            self.products[product_id] = self.products.get(product_id, repo)
        # print(self.products)
        # print(self.map)

        
    # 代码仓repoID中某种语言languageID的代码 行变化量=codeline（+增加, -减少）
    #返回 此代码仓内该语言代码的总行数
    #用例保证 代码仓已存在，一个代码仓中某语言的代码行不会减少为 负值
    def change_codelines(self,repo_id:int,language_id:int,codeline:int)->int:
        product = self.map[repo_id]
        self.products[product][repo_id][language_id] = self.products[product][repo_id].get(language_id,0)
        self.products[product][repo_id][language_id] += codeline
        print(self.products[product][repo_id][language_id])

        return self.products[product][repo_id][language_id]
    
    # 同产品product_id 所用到的各语言的代码总行数，并按要求返回语言id列表
        # product_ID为0表示所有产品。非0表示指定产品（用例保证产品存在）
        #返回要求：只返回代码量大于0的语言；优先按照语言的代码量降序；如果代码量相同，再按语言id升序。
    def stat_language(self,product_id:int)->List[int]:
        count_dic = {}

        if product_id ==0:
            # {10: {102: {2: 1800, 3: 2000}, 101: {1: 2000, 2: 200}}, 12: {122: {}}, 22: {221: {3: 500}}}
            
            for repos in self.products.values():  # repos = {102: {2: 1800, 3: 2000}, 101: {1: 2000, 2: 200}}
                for  languages  in repos.values(): # languages ={2: 1800, 3: 2000}
                    # languages = repos[rID]
                    for lanID in languages.keys():
                        count_dic[lanID] = count_dic.get(lanID,[lanID,0])
                        count_dic[lanID][1] += languages[lanID]   # hangshu = languages[lanID]
        else:
            # {102: {2: 1900}, 101: {1: 2000, 2: 200}}
            repos = self.products[product_id] 
            # print(repos)
            for  languages  in repos.values():   # repos.values = {2: 1800, 3: 2000}
                for lanID in languages.keys():
                    count_dic[lanID] = count_dic.get(lanID,[lanID,0])
                    count_dic[lanID][1] += languages[lanID]   # hangshu = languages[lanID]
                

        # print('count_dic = ',count_dic)
        sort_list = []
        for val in count_dic.values():
            if val[1] !=0:
                sort_list.append(val)
        
        sort_list = sorted(sort_list, key=lambda x:(-x[1],x[0]))

        result = []
        for aa in sort_list:
            result.append(aa[0])

        print(result)
        return result
    
# css = CodeStatsSystem([[10,[102,101]],[12,[122]],[22,[221]]]) # null
# css.change_codelines(221,3,500) # 500
# css.change_codelines(102,2,1900) # 1900
# css.change_codelines(101,1,2000) # 2000
# css.change_codelines(101,2,200) # 200
# css.stat_language(10)# [2.1]
# css.stat_language(22)# [3]
# css.change_codelines(102,3,2000) # 2000
# css.change_codelines(102,2,-100) # 1800
# css.stat_language(0) #[3,1,2 ]

css = CodeStatsSystem([[10,[102,101]]]) # null
css.stat_language(0) #[]
css.change_codelines(102,2,100) # 100
css.stat_language(0)# [2]
css.change_codelines(102,2,-100) #0
css.stat_language(0) #[]