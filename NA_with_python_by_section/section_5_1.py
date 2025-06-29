# 우측 리만 합 시각화
for i in range(n):
    x_rect_right = [x_rect[i], x_rect[i], x_rect[i+1], x_rect[i+1]]
    y_rect_right = [0, f(x_rect[i+1]), f(x_rect[i+1]), 0]
    plt.fill(x_rect_right, y_rect_right, 'b', edgecolor='k', alpha=0.3, label='Right