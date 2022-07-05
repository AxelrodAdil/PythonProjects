from deepface import DeepFace
import json


def face_verify(img_1, img_2):
    try:
        result = DeepFace.verify(img1_path=img_1, img2_path=img_2)

        with open('result_DeepFace.json', 'w') as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
        # return result

        if result.get('verified'):
            return 'YES'
        return 'NO'
    except Exception as e:
        return e


def face_recognize():
    try:
        result = DeepFace.find(img_path='resources/hl1.jpg', db_path='deepFaceDB')
        result = result.values.tolist()
        return result
    except Exception as e:
        return e


def face_analyze():
    try:
        result = DeepFace.analyze(img_path='resources/hl2.jpg', actions=['age', 'gender', 'race', 'emotion'])
        # result = DeepFace.analyze(img_path='deepFaceDB/as1.jpg', actions=['age', 'gender', 'race', 'emotion'])
        with open('result_analyze_DeepFace.json', 'w') as file:
            json.dump(result, file, indent=4, ensure_ascii=False)
        return result
    except Exception as e:
        return e


def main():
    # print(face_verify(img_1='resources/hl1.jpg', img_2='resources/hl2.jpg'))
    # print(face_recognize())
    print(face_analyze())


if __name__ == '__main__':
    main()
