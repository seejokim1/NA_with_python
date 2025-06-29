# 선 스타일 및 색상 설정
    line_styles = ['-', '--', '-.', ':']
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    # 시각화
    plt.figure(figsize=(8, 4))
    step_size = max(1, m // plot_steps)
    for i, idx in enumerate(range(1, results.shape[0], step_size)):
        style = line_styles[i % len(line_styles)]  # 선 스타일 순환
        color = colors[i % len(colors)]  # 색상 순환
        plt.plot(x, results[idx, :], linestyle=style, color=color,
                 marker='o', label=f"t={t[idx]:.2f}")
    plt.xlabel("Space (x)")
    plt.ylabel("Temperature (u)")   
    plt.title(f"1D Heat Transfer Solution ({method_name} Method)")
    # legend를 오른쪽에 배치
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)
    plt.grid(True)
    plt.tight_layout()  # 레이아웃 자동 조정
    plt.show()
# 사용자 입력