# Stepik__Page_Object

Сделал канонично по духу Page Object: ни одного assert в объектах страниц, а только в тестах.(а не наоборот, как почему-то нас пытаются научить)
В документации селениума и пейдж обжект патерна сказано, что ассерты НЕ должны быть в объектах страниц, только в тестах: 
"Page objects themselves should never make verifications or assertions. This is part of your test and should always be within the test’s code,
never in an page object. 
The page object will contain the representation of the page, and the services the page provides via methods but no code related to what is being
tested should be within the page object."

