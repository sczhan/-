from beidaqingniao.oop.supermarket.entity.admin import Admin
from beidaqingniao.oop.supermarket.entity.cashier import Cashier
from beidaqingniao.oop.supermarket.entity.user import User
from beidaqingniao.oop.supermarket.service.admin_service import AdminService
from beidaqingniao.oop.supermarket.service.cashier_service import CashierServer
from beidaqingniao.oop.supermarket.service.user_service import UserService


def admin_login():
    print("管理员登陆".center(20, "="))
    name = input("请输入管理员用户名: ")
    password = input("请输入登陆密码: ")
    admin = Admin(name=name, password=password)
    admin_service = AdminService()
    ret = admin_service.login(admin)
    return ret


def user_reg():
    print('顾客注册'.center(20, '='))
    name = input('请输入顾客ID：')
    password1 = input('请输入登陆密码：')
    password2 = input('请再次输入登陆密码：')
    if password1 != password2:
        return False
    user = User(user_id=name, password=password1)
    user_service = UserService()
    ret = user_service.reg(user)
    return ret


def user_login():
    print('顾客登陆'.center(20, '='))
    name = input('请输入顾客ID：')
    password = input('请输入登陆密码：')
    user = User(user_id=name, password=password)
    user_service = UserService()
    ret = user_service.login(user)
    return ret


def cashier_login():
    print("收银员登录".center(20, "*"))
    cashier_id = input("请输入收银员ID: ")
    password = input("请输入密码: ")
    cashier = Cashier(cashier_name=cashier_id, cashier_password=password)
    cashier_service = CashierServer()
    ret = cashier_service.login(cashier)
    return ret


def add_cashier():
    print("收银员添加")
    cashier_id = input("请输入收银员ID: ")
    password1 = input("请输入密码: ")
    password2 = input("请输入密码: ")
    if password1 != password2:
        return False
    cashier = Cashier(cashier_name=cashier_id, cashier_password=password1)
    cashier_service = CashierServer()
    ret = cashier_service.reg(cashier)
    return ret


def change_pd_cashier(cashier):
    print("修改密码: ")
    password1 = input("请输入原密码: ")
    password2 = input("请输入新密码: ")
    password3 = input("请再次输入新密码: ")
    if password1 != cashier.cashier_password:
        return False
    if password2 != password3:
        return False
    if password1 == password2:
        return False
    cashier_service = CashierServer()
    print(cashier)
    ret = cashier_service.change_pd(cashier=cashier, password=password2)
    return ret


def print_main_menu():
    print('主菜单'.center(28, '*'))
    print('1.管理员登陆')
    print('2.收银员登陆')
    print('3.顾客注册')
    print('4.顾客登陆')
    print('其它.退出')
    choice = input('请选择：')
    if choice == "1":
        rt = admin_login()
        if rt:
            print("管理员登陆成功")
            print('管理员菜单'.center(20, '='))
            print('1，添加收银员')
            print('其它.退出')
            choice = input('请选择：')
            if choice == '1':
                rt = add_cashier()
                if rt:
                    print('添加收银员成功')
                else:
                    print('添加收银员失败')
            else:
                return
        else:
            print("管理员登陆失败")
    elif choice == "2":
        rt = cashier_login()
        if rt:
            print('收银员登陆成功，请继续操作！')
            print('收银员菜单'.center(20, '='))
            print('1，修改密码')
            print('其它.退出')
            choice = input('请选择：')
            if choice == '1':
                cashier_id = input('请输入收银员用户名：')
                password = input('请输入登陆密码：')
                cashier = Cashier(cashier_name=cashier_id, cashier_password=password)
                rt = change_pd_cashier(cashier=cashier)
                if rt:
                    print('修改密码成功')

                else:
                    print('修改密码失败')
            else:
                return
        else:
            print('收银员登陆失败，请重新登陆！')
    elif choice == "3":
        rt = user_reg()
        if rt:
            print('注册成功，请登陆！')
        else:
            print('注册失败，请重新注册！')
    elif choice == "4":
        rt = user_login()
        if rt:
            print('顾客登陆成功，请继续操作！')
        else:
            print('顾客登陆失败，请重新登陆！')
    else:
        return "end"


if __name__ == '__main__':
    while True:
        rt = print_main_menu()
        if rt == "end":
            break
    # 有错误在修改中