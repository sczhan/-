# import tensorflow as tf
# import math
# tf.compat.v1.disable_eager_execution() # 保证sess.run()能够正常运行
#
# a = tf.zeros((2, 3, 4, 5), dtype=tf.float16)
#
# sess = tf.compat.v1.Session()
# sess.run(tf.rank(a))
# print(sess.run(a))
#
# T0 = tf.Variable(tf.compat.v1.random_normal([1, 3, 2, 3]), name="t")
# T = tf.Variable(tf.compat.v1.random_normal([1, 3, 2, 3]), dtype=tf.float32, name="t")
#
# # 初始化变量
# init = tf.compat.v1.global_variables_initializer()
#
# # 启动默认图
# with tf.compat.v1.Session() as sess:
#     sess.run(init)
#
#     # 张量的值
#     print("T-eval():%s\n" % T.eval())
#
#     # 张量的数据类型
#     print("T-dtype:%s\n" % T.dtype)
#
#     # 张量的名字
#     print("T-name:%s\n" % T.name)
#
#     # 重名时加序号区分
#     print("T0-name:%s\n" % T0.name)
#
#     # 张量所在的图
#     print("T-name:%s\n" % T.graph)
#
#     # 产生张量的操作
#     print("*"*50)
#     print("T-op():%s\n" % T.op)
#
#
# # Tensor的初始化
# t0 = tf.constant(10, shape=[])
# t1 = tf.constant(10, shape=[3])
# t2 = tf.zeros(shape=[2, 4])
# t3 = tf.zeros_like(t1)   # type & shape 一样，值改为0
# t4 = tf.ones(shape=[2, 5])
# t5 = tf.ones_like(t1)
# t6 = tf.fill([2, 3], 6)
# tx1 = tf.compat.v1.constant([10, 12, 13, 14, 15, 16], shape=[4, 3])
# # tx2 = tf.constant([10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], shape=[4, 3])
# tx2 = tf.compat.v1.constant([10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], shape=[4, 3])
# # tx3 = tf.compat.v1.constant([10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], shape=[3, 3])
#
# sess = tf.compat.v1.Session()
# print("scalar value t0 \n\t %s " % sess.run(t0))
# print("scalar value t1 \n\t %s " % sess.run(t1))
# print("scalar value t2 \n\t %s " % sess.run(t2))
# print("scalar value t3 \n\t %s " % sess.run(t3))
# print("scalar value t4 \n\t %s " % sess.run(t4))
# print("scalar value t5 \n\t %s " % sess.run(t5))
# print("scalar value t6 \n\t %s " % sess.run(t6))
# print("scalar value tx1 \n\t %s " % sess.run(tx1))
# print("scalar value tx2 \n\t %s " % sess.run(tx2))
# # print("scalar value tx3 \n\t %s " % sess.run(tx3))
#
# L1 = tf.linspace(10.0, 12.0, 3)
# L2 = tf.linspace(10.0, 22.0, 4)
#
# sess = tf.compat.v1.Session()
#
# print("tensor value L1 \n\t %s " % sess.run(L1))
# print("tensor value L2 \n\t %s " % sess.run(L2))
#
# # tf.range
# start = 3
# limit = 18
# delta = 2
# L3 = tf.range(start, limit, delta)
# print("tensor value L3 \n\t %s " % sess.run(L3))
#
# # 创建有随机正态值组成的形状[2, 3]张量，平均值为 -1， 标准偏差为4.
# L4 = tf.compat.v1.random_normal([2, 3], mean=-1, stddev=4)
# print("tensor value L4 \n\t %s " % sess.run(L4))
#
# # Tile, 平铺， 参见Window壁纸
# v = tf.range(1, 4)
#
# sess = tf.compat.v1.Session()
# print(sess.run(v))
#
# v3 = tf.tile(v, [3])
# print(sess.run(v3))
#
#
# def log10(x):
#     numerator = tf.compat.v1.log()
#     dencoginator = tf.compat.v1.log(tf.constant(10000, dtype=numerator.dtype))
#     return numerator, dencoginator
#
# 0
# a = log10(10000.0)
# print(a, math.log(10000, 10))
# print(tf.compat.v1.log(10000.0))
# a = ["PPCL", "DB", "Coater", "SBK", "TRF3", "", "", "Develop", "TRF4"]
# for i in range(3, 12):
#     b = a[i-3]
#     if b == "":
#         pass
#     else:
#         print("SHTM_3.5G_EQProfile_PHT_TPOT Line_Node{:02}_{}_CIM Update_20201204".format(i, b))
        # print("SHTM_3.5G_EQProfile_PHT_TPOT Line_Node{:02}_{}_20201204.xlsx".format(i, b))
print(ord("SOH"))

print(chr(2))