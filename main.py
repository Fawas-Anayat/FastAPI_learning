from fastapi import FastAPI, HTTPException
from typing import Optional ,Annotated
from pydantic import BaseModel, Field,Literal

app = FastAPI()

students = [
    {"id": 1, "name": "Fawas Anayat", "age": 22, "grade": "A", "city": "Mansehra"},
    {"id": 2, "name": "Ali Khan", "age": 21, "grade": "B", "city": "Islamabad"},
    {"id": 3, "name": "Sara Ahmed", "age": 23, "grade": "A", "city": "Lahore"},
    {"id": 4, "name": "Hassan Ali", "age": 20, "grade": "C", "city": "Karachi"},
    {"id": 5, "name": "Ayesha Iqbal", "age": 22, "grade": "B", "city": "Peshawar"},
]

class Student(BaseModel):
    id:Annotated[str,Field(...,description='.this is the id of the person ',examples='1,2,3,....')]
    name :Annotated[str,Field(min_length=5, max_length=25)]
    age: int = Field(gt=5, lt=30)
    city: str
    gender: Annotated[
        Literal['male', 'female', 'other'],
        Field(
            ...,
            description="This is the gender of the patient",
            examples={"example": "male"}
        )
    ]
    grade: Optional[str] = None

#computed fields are the special kinds of the fields that are not provided by the user but they are calculated on the spot and the provided to the other fields

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/studentData/{student_id}")
def student_data_by_id(student_id: int):
    for student in students:
        if student_id == student["id"]:
            return student
    raise HTTPException(status_code=404, detail="student not found")

@app.get("/students")
def students_filtering(
    name: Optional[str] = None,
    city: Optional[str] = None,
    grade: Optional[str] = None,
):
    results = students
    if name:
        results = [s for s in results if name.lower() in s["name"].lower()]
    if grade:
        results = [s for s in results if grade.upper() == s["grade"].upper()]
    if city:
        results = [s for s in results if city.lower() in s["city"].lower()]
    return results

@app.post("/addStudents")
def add_student(student: Student):
    for s in students:
        if student.id == s["id"]:
            raise HTTPException(status_code=400, detail="student already exists")
    students.append(student.dict())
    return {"message": "student added", "student": student}

@app.put("/updateStudents/{student_id}")
def update_student(student_id: int, student: Student):
    for i, s in enumerate(students):
        if student_id == s["id"]:
            students[i] = student.dict()
            return {"message": "student updated", "student": students[i]}
    raise HTTPException(status_code=404, detail="student not found")

# when we want to do the inference of the some of the ML model in the fastapi then we use the https method as the post.
# post is used when we want that the client send some data to the server and then server process it and infer some results from it.

