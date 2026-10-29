from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    positive_x = np.linspace(0.01, 2 * np.pi, 500)
    nonzero_x = x[np.abs(x) > 0.05]

    functions = [
        ("Linear: y = x", x, x),
        ("Quadratic: y = x²", x, x**2),
        ("Cubic: y = x³", x, x**3),
        ("Sine: y = sin(x)", x, np.sin(x)),
        ("Cosine: y = cos(x)", x, np.cos(x)),
        ("Hyperbolic tangent: y = tanh(x)", x, np.tanh(x)),
        ("Gaussian: y = exp(-x² / 2)", x, np.exp(-(x**2) / 2)),
        ("Square root: y = √|x|", x, np.sqrt(np.abs(x))),
        ("Logarithm: y = ln(x)", positive_x, np.log(positive_x)),
        ("Reciprocal: y = 1 / x", nonzero_x, 1 / nonzero_x),
    ]

    fig, axes = plt.subplots(2, 5, figsize=(18, 8))
    fig.suptitle("Ten Mathematical Functions", fontsize=18)

    for axis, (title, function_x, function_y) in zip(axes.flat, functions):
        axis.plot(function_x, function_y, color="royalblue", linewidth=2)
        axis.axhline(0, color="black", linewidth=0.7)
        axis.axvline(0, color="black", linewidth=0.7)
        axis.set_title(title)
        axis.grid(True, linestyle="--", alpha=0.4)
        axis.set_xlabel("x")
        axis.set_ylabel("y")

    fig.tight_layout(rect=(0, 0, 1, 0.94))
    output_path = Path(__file__).with_name("functions_plot.png")
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"Plot saved to {output_path}")


if __name__ == "__main__":
    main()
