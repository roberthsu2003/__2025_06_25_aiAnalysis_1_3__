#有一個names.txt
#讀取names.txt
#請隨機取出3個名字
import random



random.seed(4561)

def sample_names_from_file(file_name: str, nums: int = 1) -> list[str]:
    """
    從指定的檔案中讀取所有姓名，並隨機取出指定數量的姓名。

    參數:
        file_name (str): 檔案名稱，檔案內容為姓名，每行一個。
        nums (int): 要隨機取出的姓名數量，預設為1。

    回傳:
        list[str]: 隨機取出的姓名列表。
    """
    try:
        with open(file_name, encoding="utf-8") as file:
            content: str = file.read()
            names: list[str] = content.split()
            if not names:
                raise ValueError("檔案內容為空，無法取出姓名。")
            return random.sample(names, nums)
    except FileNotFoundError:
        print(f"檔案 {file_name} 不存在，請檢查檔案路徑。")
        return []
    except ValueError as e:
        print(e)
        return []

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
        for subject in ["國文", "英文", "數學"]:
            student_scores[subject] = random.randint(50, 100) 
        result_list.append(student_scores)

    return result_list


def print_student_scores(students: list[dict]):
    '''列印學生姓名和分數，並計算平均分數。
    參數:
        students (list[dict]): 包含學生姓名和分數的列表。
    
    回傳:
        None
    '''    
    print("學生成績表:")
    print("姓名\t國文\t英文\t數學\t平均")
    for student in students:
        name = student["姓名"]
        scores:list[int] = [student[subject] for subject in ["國文", "英文", "數學"]]        
        average = sum(scores) / len(scores)
        print(f"{name}\t{scores[0]}\t{scores[1]}\t{scores[2]}\t{average:.2f}")


def analyze_scores(students: list[dict]):
    """
    分析學生的成績，列印全班平均成績、最高分學生及最低分學生。

    參數:
        students (list[dict]): 包含學生姓名和分數的列表。

    回傳:
        None
    """
    total_scores = []
    highest_student = None
    lowest_student = None

    for student in students:
        scores = [student[subject] for subject in ["國文", "英文", "數學"]]
        total_scores.extend(scores)
        average_score = sum(scores) / len(scores)

        if not highest_student or average_score > highest_student["平均分數"]:
            highest_student = {"姓名": student["姓名"], "平均分數": average_score}

        if not lowest_student or average_score < lowest_student["平均分數"]:
            lowest_student = {"姓名": student["姓名"], "平均分數": average_score}

    class_average = sum(total_scores) / len(total_scores)

    print("成績分析:")
    print(f"- 全班平均成績:{class_average:.1f}分")
    print(f"- 最高分學生: {highest_student['姓名']}({highest_student['平均分數']:.1f}分)")
    print(f"- 最低分學生: {lowest_student['姓名']}({lowest_student['平均分數']:.1f}分)")


def main():
    print("=== 學生成績管理系統 ===\n\n")
    names: list[str] = sample_names_from_file("names.txt", nums=3)
    if not names:
        return
    students: list[dict] = generate_scores_for_names(names)
    print_student_scores(students)
    analyze_scores(students)  # 新增分析成績的功能

if __name__ == "__main__":
    main()