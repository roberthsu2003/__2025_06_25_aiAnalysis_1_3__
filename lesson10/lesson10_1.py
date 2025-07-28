def get_bmi()->float:
    '''
    建立身高,體重的輸入
    計算BMI
    return:bmi的值(float)
    '''
    height = float(input('請輸入身高 (120~250 cm): '))
    if not (120 <= height <= 250):
        print('身高範圍輸入錯誤')
        raise Exception

    weight = float(input('請輸入體重 (30~200 kg): '))
    if not (30 <= weight <= 200):
        print('體重範圍輸入錯誤')
        raise Exception

    BMI = weight / ((height / 100) ** 2)
    return BMI


def get_status(BMI):
    '''
    根據BMI值，判斷體重狀態
    :param BMI: float, 計算出的BMI值
    '''
    print('你的 BMI 為:', round(BMI, 1))

    if BMI < 18.5:
        x = '體重過輕'
    elif 18.5 <= BMI < 24:
        x = '正常範圍'
    elif 24 <= BMI < 27:
        x = '體重過重'
    elif 27 <= BMI < 30:
        x = '輕度肥胖'
    elif 30 <= BMI < 35:
        x = '中度肥胖'
    else:
        x = '重度肥胖'

    print('您的體重狀態為：', x)


def main():
    while True:
        try:
            bmi = get_bmi()         
            get_status(bmi)

        except ValueError:
            print('請輸入數字（身高、體重）')
            continue
        except Exception:
            print('輸入錯誤，請重新輸入')
            continue
        finally:
            print('--- 應用程式結束 ---')

        break


if __name__ == "__main__":
    main()