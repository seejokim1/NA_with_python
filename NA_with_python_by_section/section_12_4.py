plt.figtext(0.15, 0.5, r"$u(0) = 1, \, u(1) = \exp(1)$", fontsize=12, color="purple")
    plt.xlabel("x")
    plt.ylabel("ODE Solution")
    plt.legend()
    plt.title("Comparison of exact and FEM solutions with ODE and Boundary Conditions")
    plt.grid()
    plt.show()
if __name__ == "__main__":
    main()