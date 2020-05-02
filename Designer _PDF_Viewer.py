#for more information copy this link: https://www.hackerrank.com/challenges/designer-pdf-viewer/problem

def designerPdfViewer(h, word):
    max_height = 0
    for i in range(len(word)):
        num = h[ord(word[i]) - 97]
        if(num > max_height):
            max_height = num
    last_result = max_height * len(word)
    return(last_result)

if __name__ == '__main__':

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(result)
