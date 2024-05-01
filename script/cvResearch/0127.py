from sklearn.model_selection import train_test_split
import tensorflow as tf
x_data='' # 數據集
y_labels='' # 測試標籤
x_train,x_test,y_train,y_test = train_test_split(x_data,y_labels,test_size=0.25,random_state=33)
step_cnt=10000 # 訓練模型的迭代步數
batch_size = 100
learning_rate = 0.001
x=tf.compat.v1.placeholder("float",shape=[None,784])
y_ = tf.compat.v1.placeholder("float",shape=[None,10])
x_image = tf.reshape(x,[-1,28,28,1])
keep_prob = tf.compat.v1.placeholder(tf.float32)
conv1_weight = tf.compat.v1.get_variable("conv1_weights",[5,5,1,32],initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.1))
conv1_biases = tf.compat.v1.get_variable("conv1_biases",[32],initializer=tf.compat.v1.constant_initializer(0.0))
conv1 = tf.compat.v1.nn.conv2d(x_image,conv1_weight,strides=[1,1,1,1],padding='SAME')
relu1=tf.compat.v1.nn.bias_add(conv1,conv1_biases)

pool1=tf.compat.v1.nn.max_pool(relu1,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

conv2_weights = tf.compat.v1.get_variable("conv2_weights",[5,5,32,64],initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.1))
conv2_biases = tf.compat.v1.get_variable("conv2_biases",[64],initializer=tf.compat.v1.constant_initializer(0.0))
conv2 = tf.compat.v1.nn.conv2d(pool1,conv2_weights,strides=[1,1,1,1],padding='SAME')
relu2=tf.compat.v1.nn.relu(tf.compat.v1.nn.bias_add(conv2,conv2_biases))
pool2 = tf.compat.v1.nn.max_pool(relu2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')
fcl_weights=tf.compat.v1.get_variable("fcl_weights",[7,7,64,1024],initializer=tf.compat.v1.truncated_normal_initializer(stddev=0.1))
