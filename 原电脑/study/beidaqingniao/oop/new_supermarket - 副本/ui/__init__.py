from beidaqingniao.oop.new_supermarket.entity.account import Account
from beidaqingniao.oop.new_supermarket.entity.admin import Admin
from beidaqingniao.oop.new_supermarket.entity.item import Item
from beidaqingniao.oop.new_supermarket.entity.order import Order
from beidaqingniao.oop.new_supermarket.entity.user import User
from beidaqingniao.oop.new_supermarket.service.account_service import AccountService
from beidaqingniao.oop.new_supermarket.service.admin_service import AdminService
from beidaqingniao.oop.new_supermarket.service.item_service import ItemService
from beidaqingniao.oop.new_supermarket.service.order_service import OrderService
from beidaqingniao.oop.new_supermarket.service.return_item_service import ReturnItemService
from beidaqingniao.oop.new_supermarket.service.user_service import UserService
from beidaqingniao.oop.new_supermarket.utils.util import account_float, account_int

current_person = None


def admin_login():
    global current_person
    print("管理员登录".center(20, "="))
    name = input("请输入管理员名称: ")
    password = input("请输入管理员密码: ")
    admin = Admin(name, password)
    admin_service = AdminService()
    ret = admin_service.login(admin)
    if ret:
        current_person = admin
    return ret


def add_account():
    print('添加收银员'.center(20, '='))
    name = input('请输入收银员ID：')
    password1 = input('请输入登陆密码：')
    password2 = input('请再次输入登陆密码：')
    if password1 != password2:
        return False
    account = Account(name, password1)
    account_service = AccountService()
    ret = account_service.add(account)
    return ret


def delete_account():
    name = input('请输入要删除的收银员账号id：')
    account_service = AccountService()
    ret = account_service.remove(name)
    return ret


def account_login():
    global current_person
    print('收银员登陆'.center(20, '='))
    name = input('请输入收银员ID：')
    password = input('请输入登陆密码：')
    account = Account(name, password)
    account_service = AccountService()
    ret = account_service.login(account)
    if ret:
        current_person = account
    return ret


def query_user():
    user_service = UserService()
    users = user_service.query_all()
    for u in users:
        print(u)


def modify_account_password():
    # 以下判断在终端程序中可以省略
    if not isinstance(current_person, Account):
        return False
    old_pass = input('请输入旧密码：')
    password1 = input('请输入新密码：')
    password2 = input('请再次输入新密码：')
    if password1 != password2:
        return False
    if old_pass != current_person.password:
        return False
    account_service = AccountService()
    ret = account_service.modify(current_person, password1)
    return ret


def user_reg():
    print("顾客注册".center(20, "="))
    name = input("请输入顾客名称: ")
    password1 = input("请输入顾客密码: ")
    password2 = input("请再次输入密码: ")
    if password2 != password1:
        return False
    user = User(name, password1)
    user_service = UserService()
    ret = user_service.reg(user)
    return ret


def user_login():
    global current_person
    print("顾客登录".center(20, "="))
    name = input("请输入顾客名称: ")
    password = input("请输入顾客密码: ")
    user = User(name, password)
    user_service = UserService()
    ret = user_service.login(user)
    if ret:
        current_person = user
    return ret


def add_item():
    id = input('请输入商品编号：')
    title = input('请输入商品名称：')
    stock = account_int('请输入商品数量：')
    price = account_float('请输入商品价格：')
    item = Item(id, title, stock, price)
    item_service = ItemService()
    ret = item_service.add(item)
    return ret


def query_item():
    item_service = ItemService()
    items = item_service.query_all()
    for i in items:
        print(i)


def enter_admin_menu():
    while True:
        rt = print_admin_menu()
        if rt == 'end':
            break


def add_order():
    user_service = UserService()
    while True:
        user_id = input('请输入顾客id')
        if user_id != user_service.find_user_id(user_id):
            print("顾客不存在, 请重新输入顾客名称")
            continue
        if user_id == user_service.find_user_id(user_id):
            break
    carts = []
    item_service = ItemService()
    while True:
        item_id = input('请输入商品编号：')
        price = item_service.find_price(item_id)
        if price is None:
            print('商品不存在！')
            continue
        quantity = account_int('请输入购买数量: ')
        item = Item(id=item_id, stock=quantity, price=price, title='')
        carts.append(item)
        echo = input('是否继续？y/n')
        if echo == 'n':
            break
    order = Order(user_id, carts)
    order_service = OrderService()
    print("商品总价格: ", order_service.price(order))
    print("商品清单: ", order_service.item_order(order))
    return order_service.add(order)


def return_sno():
    return_service = ReturnItemService()
    return_sno = int(input('请输入退单号'))
    if return_sno == return_service.return_item_name(return_sno):
        return_order = return_service.return_item_sno(return_sno)
        return return_service.return_item(return_order)
    else:
        print(1)

def print_admin_menu():
    print('管理员子菜单'.center(28, '-'))
    print('1.添加收银员')
    print('2.修改收银员')
    print('3.删除收银员')
    print('4.顾客查询')
    print('5.商品添加')
    print('6.商品查询')
    print('7.退货')
    print('其它.返回上级')
    choice = input('请选择：')
    if choice == '1':
        rt = add_account()
        if rt:
            print('添加收银员成功')
        else:
            print('添加收银员失败')

    elif choice == '2':
        pass
    elif choice == '3':
        rt = delete_account()
        if rt:
            print('删除收银员成功！')
        else:
            print('删除收银员失败！')

    elif choice == '4':
        query_user()
    elif choice == '5':
        rt = add_item()
        if rt:
            print('添加商品成功！')
        else:
            print('添加商品失败！')
    elif choice == '6':
        query_item()
    elif choice == '7':
        rt = return_sno()
        if rt:
            print('退货成功！')
        else:
            print('退货失败！')
    else:
        return 'end'


def print_account_menu():
    print('收银员子菜单'.center(28, '-'))
    print('1.收银')
    print('2.修改密码')
    print('其它.返回上级')
    choice = input('请选择：')
    if choice == '1':
        rt = add_order()
        if rt:
            print('收银成功')
        else:
            print('收银失败')
    elif choice == '2':
        rt = modify_account_password()
        if rt:
            print('收银员修改密码成功')
        else:
            print('收银员修改密码失败')
    else:
        return 'end'


def print_main_menu():
    print('主菜单'.center(28, '*'))
    print('1.管理员登陆')
    print('2.收银员登陆')
    print('3.顾客注册')
    print('4.顾客登陆')
    print('其它.退出')
    choice = input('请选择：')
    if choice == '1':
        rt = admin_login()
        if rt:
            print('管理员登陆成功')
            enter_admin_menu()
        else:
            print('管理员登陆失败')
    elif choice == "2":
        rt = account_login()
        if rt:
            print('收银员登陆成功')
            print_account_menu()
        else:
            print('收银员登陆失败')
    elif choice == "3":
        rt = user_reg()
        if rt:
            print("顾客注册成功")
        else:
            print("顾客注册失败, 请重新注册")
    elif choice == "4":
        rt = user_login()
        if rt:
            print("顾客登录成功")
        else:
            print("顾客登录失败")
    else:
        return "end"


if __name__ == '__main__':
    while True:
        rt = print_main_menu()
        if rt == "end":
            break
