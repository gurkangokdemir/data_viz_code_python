%matplotlib tk

fig, ax = plt.subplots()
for x in range(train_X.shape[0]):
    ax.clear()
    ax.imshow([i for i in 255 - train_X[x].T], cmap='gray') #all data is flipped over, so we use T for transpose
    title = 'label %d = %s' %(train_y[x],labels[train_y[x]])
    ax.set_title(title,fontsize=20)
    plt.pause(1)
