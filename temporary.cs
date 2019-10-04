using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class NewBehaviourScript : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
    dictIn = askData();
    dictOut = ApiPostBackend(dictIn);
    if (dictOut.id_user)
        {
            

        }
    else
        {
            BoxTxt("Review the inputs")
        }
    }

public function Combinations(str1, str2, str3): MonoBehaviour
{
    if(String.Compare(str1, str2) == 0)
    {
        if(String.Compare(str2, str3) == 0)
        {
            if(String.Compare(str2, '001') == 0) 
            {
                BoxTxt("Congratulations !!!");
            }
            else if (String.Compare(str2, '002') == 0)
            {
                BoxTxt("Follow the framework");            
            }
            else if (String.Compare(str2, '003') == 0)
            {
                BoxTxt("Don't be late")
            }
            else if (String.Compare(str2, '004') == 0)
            {
                BoxTxt("DevOps is AMAZING !!!")
            }
            else if (String.Compare(str2, '005') == 0)
            {
                BoxTxt("C is Fun")
            }
            else if (String.Compare(str2, '006') == 0)
            {
                BoxTxt("Python is cool!!!")
            }
            else if (String.Compare(str2, '007') == 0)
            {
                BoxTxt("JS is amazing")
            }
            else if (String.Compare(str2, '008') == 0)
            {
                BoxTxt("Ubuntu is nice")
            }
            else if (String.Compare(str2, '009') == 0)
            {
                BoxTxt("HBN the Best")
            }
        }
        else
        // if str2 != str 3 but str1 = str2
        {
            if(String.Compare(str2, '001') == 0) 
            {
                BoxTxt("Well done");
            }
            else if (String.Compare(str2, '002') == 0)
            {
                BoxTxt("Keep trying");            
            }
            else if (String.Compare(str2, '003') == 0)
            {
                BoxTxt("Keep trying")
            }
            else if (String.Compare(str2, '004') == 0)
            {
                BoxTxt("Keep trying")
            }
            else if (String.Compare(str2, '005') == 0)
            {
                BoxTxt("Go to programming")
            }
            else if (String.Compare(str2, '006') == 0)
            {
                BoxTxt("Go to programming")
            }
            else if (String.Compare(str2, '007') == 0)
            {
                BoxTxt("Go to programming")
            }
            else if (String.Compare(str2, '008') == 0)
            {
                BoxTxt("Go to programming")
            }
            else if (String.Compare(str2, '009') == 0)
            {
                BoxTxt("Keep trying")
            }
        }
    else if (String.Compare(str1, str3) == 0)
    {
       if(String.Compare(str1, '001') == 0) 
            {
                BoxTxt("Well done");
            }
            else if (String.Compare(str1, '002') == 0)
            {
                BoxTxt("Keep trying");            
            }
            else if (String.Compare(str1, '003') == 0)
            {
                BoxTxt("Keep trying")
            }
            else if (String.Compare(str1, '004') == 0)
            {
                BoxTxt("Keep trying")
            }
            else if (String.Compare(str1, '005') == 0)
            {
                BoxTxt("Go to programming")
            }
            else if (String.Compare(str1, '006') == 0)
            {
                BoxTxt("Go to programming")
            }
            else if (String.Compare(str1, '007') == 0)
            {
                BoxTxt("Go to programming")
            }
            else if (String.Compare(str1, '008') == 0)
            {
                BoxTxt("Go to programming")
            }
            else if (String.Compare(str1, '009') == 0)
            {
                BoxTxt("Keep trying")
            } 
    }
    else if (String.Compare(str2, str3) == 0) 
    {
        if(String.Compare(str2, '001') == 0) 
            {
                BoxTxt("Well done");
            }
            else if (String.Compare(str2, '002') == 0)
            {
                BoxTxt("Keep trying");            
            }
            else if (String.Compare(str2, '003') == 0)
            {
                BoxTxt("Keep trying")
            }
            else if (String.Compare(str2, '004') == 0)
            {
                BoxTxt("Keep trying")
            }
            else if (String.Compare(str2, '005') == 0)
            {
                BoxTxt("Go to programming")
            }
            else if (String.Compare(str2, '006') == 0)
            {
                BoxTxt("Go to programming")
            }
            else if (String.Compare(str2, '007') == 0)
            {
                BoxTxt("Go to programming")
            }
            else if (String.Compare(str2, '008') == 0)
            {
                BoxTxt("Go to programming")
            }
            else if (String.Compare(str2, '009') == 0)
            {
                BoxTxt("Keep trying")
            }
    }
    else
    {
        BoxTxt("Segmentation Fault: Try Again")
    }
}

public function askData()
{
    dictIn = {"email": "789@holbertonschool.com",
               "pass": "12345",
               "api_key": "6249dec5a1d06c60a7fbacbfe3f63015"}
    return(dictIn)
}


public function BoxTxt(str)
{

}

public void ApiPostBackend(dictIn)
{
    try
    {
        string url = "http://34.74.88.31:5001/api/user/";

        var request = UnityWebRequest.Post(url, "");
        request.SetRequestHeader("Content-Type", "application/json");
        request.SetRequestHeader("email", dictIn.email);
        request.SetRequestHeader("password", dictIn.password);
        request.SetRequestHeader("api_key", dictIn.api_key);

        StartCoroutine(onResponse(request));
    }
    catch (Exception e) { Debug.Log("ERROR : " + e.Message); }
}
private IEnumerator onResponse(UnityWebRequest req)
{
    yield return req.SendWebRequest();
    if (req.isError)
      Debug.Log("Network error has occured: " + req.GetResponseHeader(""));
    else
        Debug.Log("Success "+req.downloadHandler.text );
        byte[] results = req.downloadHandler.data;
        Debug.Log("Answer from API Backend" + results);
    Debug.Log("Second Success");
    // Some code after success
}
