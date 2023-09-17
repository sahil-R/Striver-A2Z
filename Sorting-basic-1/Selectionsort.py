from typing import List

def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    for i in range(len(arr)-1):
        pos=i+1
        minimum=arr[pos]
        j=pos
        while j<len(arr):
            if minimum>arr[j]:
                pos=j
                minimum=arr[j]
            j+=1
        if arr[i]>arr[pos]:
            temp=arr[i]
            arr[i]=arr[pos]
            arr[pos]=temp
        # print(arr)
    
# import java.util.*;

# public class tUf {
#     static void selection_sort(int arr[], int n) {
#         for (int i = 0; i < n - 1; i++) {
#             int mini = i;
#             for (int j = i + 1; j < n; j++) {
#                 if (arr[j] < arr[mini]) {
#                     mini = j;
#                 }
#             }
#             //swap
#             int temp = arr[mini];
#             arr[mini] = arr[i];
#             arr[i] = temp;
#         }

#         System.out.println("After selection sort:");
#         for (int i = 0; i < n; i++) {
#             System.out.print(arr[i] + " ");
#         }
#         System.out.println();
#     }

#     public static void main(String args[]) {

#         int arr[] = {13, 46, 24, 52, 20, 9};
#         int n = arr.length;
#         System.out.println("Before selection sort:");
#         for (int i = 0; i < n; i++) {
#             System.out.print(arr[i] + " ");
#         }
#         System.out.println();
#         selection_sort(arr, n);
#     }
# }