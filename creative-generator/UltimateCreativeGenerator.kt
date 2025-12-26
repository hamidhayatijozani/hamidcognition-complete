/**
 * UltimateCreativeGenerator.kt
 * سیستم "بازیکن آزاد" تولید تابع خلاق
 */

class UltimateCreativeGenerator {
    fun generateCreativeInsight(p: Double, s: Double, t: Double): String {
        val energy = (p * s) / (1.1 - t)
        return when {
            energy > 1.2 -> "SYNTHESIS PEAK: Creative explosion imminent."
            p > s -> "POWER DOMINANCE: Deep penetration into market structure."
            s > p -> "SYNCHRONICITY: High creative connection with global trends."
            else -> "STEADY STATE: Exploring stable patterns."
        }
    }
}

fun main() {
    val generator = UltimateCreativeGenerator()
    println(generator.generateCreativeInsight(0.88, 0.78, 0.40))
}
