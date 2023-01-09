FROM python:3.10

# apt-getのバージョンを更新する
RUN apt-get update

# コンテナ上のワーキングディレクトリを指定する
WORKDIR /usr/src/backend

# ディレクトリとファイルをコピーする
COPY apis /usr/src/backend/apis
COPY apis/app.py /usr/src/backend/app.py
COPY requirements.txt /usr/src/backend/requirements.txt

# pipのバージョンを更新する
RUN pip install --upgrade pip

# 必要なライブラリをコンテナ内の環境にインストールする
RUN pip install -r requirements.txt

# 処理中に"building"と表示する
RUN echo "building..."

# 必要な環境変数を設定する
ENV FLASK_APP "apis.app"
ENV FLASK_CONFIG_MODE "development"

# 特定のネットワーク・ポートをコンテナが実行時にlistenする
EXPOSE 5000

# "docker run"実行時に実行されるコマンド
CMD ["flask", "run", "-h", "0.0.0.0"]


