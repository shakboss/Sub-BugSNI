{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM5XlMYrYXu9n4lYa/x38Ve",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/victorgeel/Sub-BugSNI/blob/main/Bugscanner.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# • Install Subfinder!!\n",
        "•• Usage များတယ် နည်းနည်းကြာပါတယ် ••"
      ],
      "metadata": {
        "id": "TDdEZm5V-urj"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!add-apt-repository ppa:longsleep/golang-backports -y\n",
        "!apt update\n",
        "!apt install golang-go\n",
        "%env GOPATH=/root/go\n",
        "!go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest\n",
        "!cp ~/go/bin/subfinder /usr/bin/\n",
        "!mkdir /usr/local/share/jupyter/kernels/subfinder\n",
        "!cp ~/go/pkg/mod/github.com/projectdiscovery/subfinder/v2@v2.6.3/kernel/* \\\n",
        "       /usr/local/share/jupyter/kernels/subfinder"
      ],
      "metadata": {
        "id": "CVutPspsfKGk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# ••🅰️ Install Bugscanner••\n",
        "• cmd 🅰️ ကိုသုံးရင် အောက်က ••cmd 🅱️ မလို..."
      ],
      "metadata": {
        "id": "qwaOurP1_0x5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!python3 -m pip install bugscanner"
      ],
      "metadata": {
        "id": "0jQcRQm8jT9T"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Upgrade Bugscanner"
      ],
      "metadata": {
        "id": "i4-d-9oKNAE9"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!python3 -m pip install --upgrade bugscanner"
      ],
      "metadata": {
        "id": "TK_vaCZ6M36A"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Run Subfinder\n",
        ". 🇲🇲🇲🇲🇲🇲 နေရာမှာ ရှာချင်တဲ့ Host ထည့်ပေးပါ..\n",
        "\n",
        "sub.com.txt file ကို ကြိုက်ရာနာမည်ပြောင်းပါ"
      ],
      "metadata": {
        "id": "tpOtt9GZBP87"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!subfinder -d 🇲🇲🇲🇲🇲🇲 -o sub.com.txt"
      ],
      "metadata": {
        "id": "yGMUvVdhnnuz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 🅱️ Install Bugscanner\n",
        ".. Install by Git clone..."
      ],
      "metadata": {
        "id": "JkL-fCAuB3Yo"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/aztecrabbit/bugscanner\n",
        "%cd bugscanner\n",
        "!python -m pip install -r requirements.txt\n",
        "!python setup.py install"
      ],
      "metadata": {
        "id": "LjL_6jDlwHit"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Run Bugscanner\n",
        "Run and Check your Results...\n",
        "\n",
        "🟢🟢 Enjoy 🟢🟢"
      ],
      "metadata": {
        "id": "yNJDKHsxCs4z"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install loguru\n",
        "!bugscanner /content/sub.com.txt"
      ],
      "metadata": {
        "id": "bYBUB7SOzfcu"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
