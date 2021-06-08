def body_mass_index(height: float, weight: float):
    bmi = weight / height ** 2            # 计算bmi
    if 18.5 <= bmi <= 23.9:
        return "正常", "BMI: %-.2f" % bmi    # 返回bmi
    if bmi > 23.9:
        return "偏胖", "BMI: %-.2f" % bmi
    return "偏瘦", " BMI: %-.2f" % bmi


if __name__ == '__main__':
    a = body_mass_index(1.7, 60.2)
    print(a)

# height = float(input("请输入身高(m): "))  # 也可以输入身高体重
# weight = float(input("请输入体重(kg): "))
# a = body_mass_index(height, weight)
# print(a)


