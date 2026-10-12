Attribute VB_Name = "CollectNAV"
' 월말 운용사 보고 파일(xlsx)들에서 NAV를 모아 '약정·NAV' 시트를 갱신한다
' 전제: 각 보고 파일의 첫 시트 B2 = 펀드ID, B5 = 기말 NAV
Option Explicit

Sub CollectNAV()
    Dim folder As String, f As String, wb As Workbook
    Dim ws As Worksheet, hit As Range, n As Long
    folder = ThisWorkbook.Path & "\GP_reports\"
    Set ws = ThisWorkbook.Sheets("약정·NAV")
    f = Dir(folder & "*.xlsx")
    Application.ScreenUpdating = False
    Do While f <> ""
        Set wb = Workbooks.Open(folder & f, ReadOnly:=True)
        Set hit = ws.Columns("A").Find(wb.Sheets(1).Range("B2").Value, LookAt:=xlWhole)
        If Not hit Is Nothing Then
            ws.Cells(hit.Row, "E").Value = wb.Sheets(1).Range("B5").Value
            n = n + 1
        End If
        wb.Close SaveChanges:=False
        f = Dir()
    Loop
    Application.ScreenUpdating = True
    MsgBox n & "개 펀드의 NAV를 갱신했습니다.", vbInformation
End Sub
