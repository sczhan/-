from __future__ import print_function, division

import tensorflow as tf

g = tf.Graph()
with g.as_default():
    x = tf.compat.v1.placeholder(dtype=tf.float32, name="x")
    a = tf.constant(1.0, name="a")
    b = tf.constant(3, dtype=tf.float32, name="b")
    y = x * a + b

print([node.name for node in g.as_graph_def().node])

from graphviz import Digraph


def tf_to_dot(graph):
    dot = Digraph()
    for n in g.as_graph_def().node:
        dot.node(n.name, labels=n.name)
        for i in n.input:
            dot.edge(i, n.name)
    return dot


# tf_to_dot(g).view()


# 执行
with tf.compat.v1.Session(graph=g) as sess:
    init_op = tf.compat.v1.global_variables_initializer()
    sess.run(init_op)
    r1 = sess.run(y, feed_dict={x:3})

print(r1)

