#有一個names.txt
#讀取names.txt
#請隨機取出3個名字
import random


random.seed(111)

def sample_names_from_file(file_name: str, nums: int = 1) -> list[str]:
    """
    從指定的檔案中讀取所有姓名，並隨機取出指定數量的姓名。

    參數:
        file_name (str): 檔案名稱，檔案內容為姓名，每行一個。
        nums (int): 要隨機取出的姓名數量，預設為1。

    回傳:
        list[str]: 隨機取出的姓名列表。
    """
    with open(file_name, encoding="utf-8") as file:
        content: str = file.read()
        names: list[str] = content.split()
        return random.sample(names, nums)

def generate_scores_for_names(names: list[str]) -> list[dict]:
    """
    為每個姓名生成3個隨機分數。

    參數:
        names (list[str]): 姓名列表。

    回傳:
        list[dict]: 包含姓名和3個隨機分數的2維列表。
    """
    result_list = []

    for person_name in names:
        student_scores:dict = {"姓名":person_name}
        total = 0
        for subject in ["國文", "英文", "數學"]:
            student_scores[subject] = random.randint(50, 100) 
            total += student_scores[subject]
        student_scores["平均成績"] = round(total / 3, 1)
        result_list.append(student_scores)

    return result_list

def analyze_students(result_list:list[dict]):
    """分析學生分數，計算全班平均成績、最高分和最低分。

    參數:
        result_list (list[dict]): 學生分數列表。
    回傳:
        平均成績avg:float,最高分highest:dict,最低分lowest:dict。
    """
    
    avg = sum([_['平均成績'] for _ in result_list]) / len(result_list)
    highest = max(result_list, key=lambda x: x['平均成績'])
    lowest = min(result_list, key=lambda x: x['平均成績'])    
    return avg, highest, lowest


def print_score_table(students:list[dict]):
    """列印學生分數表。

    參數:
        students (list[dict]): 學生分數列表。
    """
    print('\n學生成績表:')
    print(f"{'姓名':<8}{'國文':<6}{'英文':<6}{'數學':<6}{'平均成績':<6}")
    for i in students:
        print(f"{i['姓名']:<8}{i['國文']:<8}{i['英文']:<8}{i['數學']:<8}{i['平均成績']:<8}")

def print_analysis(avg:float, highest:dict, lowest:dict):
    """列印成績分析結果。
    參數:
        avg (float): 全班平均成績。
        highest (dict): 最高分學生的資料。
        lowest (dict): 最低分學生的資料。
    """
    
    print('\n成績分析:')
    print(f"- 全班平均成績: {avg:.1f} 分")
    print(f"- 最高分學生: {highest['姓名']} ({highest['平均成績']:.1f} 分)")
    print(f"- 最低分學生: {lowest['姓名']} ({lowest['平均成績']:.1f} 分)")


def main():
    print('=== 學生成績管理系統 ===')
    names: list[str] = sample_names_from_file("names.txt", nums=3)
    students: list[dict] = generate_scores_for_names(names)
    avg, highest, lowest = analyze_students(students)
    print_score_table(students)
    print_analysis(avg, highest, lowest)


if __name__ == "__main__":
    main()