
#include <avr/io.h>
#include <util/delay.h>

int main()
{
    DDRB |= (1 << PINB7);

    while (true) {
        PORTB ^= (1 << PINB7);

        _delay_ms(500);
    }
}
