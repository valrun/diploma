from matplotlib import pyplot as plt


def draw_lena(images, text):
    n = len(images)
    fig, ax = plt.subplots(ncols=2, nrows=n)
    for i, img_cyc in enumerate(images):
        ax[i][1].imshow(img_cyc, cmap='gray')
        ax[i][1].axis('off')
        ax[i][0].axis('off')
        ax[i][0].text(0, 0, text[i])
    plt.subplots_adjust(left=0.03, bottom=0.03, right=0.97, top=0.97)
    plt.show()