import uvicorn

from app.api.v1.routes import create_app

app = create_app()

if __name__ == "__main__":
    uvicorn.run(app)
    #uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", use_colors=True)


nums = [0,1,0,3,12]
for i in nums:
    if i==0:
      nums.pop()
      print(nums)