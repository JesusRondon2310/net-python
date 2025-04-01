from src.utils import worker

worker("echo Memory: $(free -h | awk '/Mem:/ {print $3 \"/\" $2}')", 5)
