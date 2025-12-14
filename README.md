# IoT 水位偵測自動關閉冷氣
作者：113453015 黃景偉

---

## 專案背景
因某些無法變更之限制，導致原本外接排水管斜度不足，因而排水異常，造成冷氣室內機漏水，在冷氣師傅建議下，改回傳統以水桶接水方式改冷氣漏水。

改以水桶接水方式後，延伸出另一個問題，常常水滿了而不知情，發現時已是滿地積水，造成生活上困擾，故想透過此專案進行問題改善。
<p align="center">
   <img src="images/001.JPEG" width="700" alt="環境照片">
</p>

<p align="center">
    <img src="images/002.JPEG" width="700" alt="環境照片">
</p>
---

## 專案介紹
透過樹梅派設計一個水位偵測警報與回應機制，當偵測到水位來到一定高度時（例如：八分滿），透過蜂鳴器來警示該倒水了；如果沒有任何回應，水位持續上升到最後警戒值（例如：九分滿），則觸發安全機制，自動關閉冷氣機。

---

## 裝置照片


<p align="center">
  <img src="images/003.JPEG" width="700" alt="裝置照片">
</p>

<p align="center">
  <img src="images/004.JPEG" width="700" alt="裝置照片">
</p>

---

## 專案硬體所需材料
1. Rasberry Pi 4  
2. 水位偵測器（乾接點）  
3. 5V 繼電器  
4. 蜂鳴器  
5. 麵包版  
6. 杜邦線  
7. 紅外線發射器（以遙控器取代）

<p align="center">
  <img src="images/005.JPEG" width="700" alt="材料">
</p>
<p align="center">
  <img src="images/006.JPEG" width="700" alt="材料">
</p>
<p align="center">
  <img src="images/007.JPEG" width="700" alt="材料">
</p>



---

## 電路配置圖
<p align="center">
  <img src="images/008.png" width="700" alt="材料">
</p>

---

## 程式碼功能介紹

### 1) 針對水位偵測器進行初始值設定
```python
# 第1顆水位偵測：用內建拉高電阻
GPIO.setup(WATER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 第2顆水位偵測：同樣用內建拉高電阻
GPIO.setup(WATER2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)



