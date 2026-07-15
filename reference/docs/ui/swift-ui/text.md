---
title: "Text"
description: "A SwiftUI Text component for displaying styled text with support for nested texts."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/text.md"
scraped_at: "2026-07-15T08:59:31.041923"
---

---
title: Text
description: A SwiftUI Text component for displaying styled text with support for nested texts.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Text

A SwiftUI Text component for displaying styled text with support for nested texts.
iOS, tvOS, Included in Expo Go

> For cross-platform usage, see the universal [`Text`](/versions/latest/sdk/ui/universal/text.md) — it renders the appropriate native component per platform.

Expo UI Text matches the official SwiftUI [Text API](https://developer.apple.com/documentation/swiftui/text).

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Basic text

```tsx
import { Host, Text } from '@expo/ui/swift-ui';

export default function BasicTextExample() {
  return (
    <Host matchContents>
      <Text>Hello world</Text>
    </Host>
  );
}
```

### Text with modifiers

Use modifiers to style the entire text.

```tsx
import { Host, Text } from '@expo/ui/swift-ui';
import { font, foregroundStyle } from '@expo/ui/swift-ui/modifiers';

export default function StyledTextExample() {
  return (
    <Host matchContents>
      <Text modifiers={[font({ size: 24, weight: 'bold' }), foregroundStyle('blue')]}>
        Large Bold Blue Text
      </Text>
    </Host>
  );
}
```

### Nested text (per-segment styling)

Nest `Text` components to style individual segments differently. This is useful for inline formatting, such as bold or colored words within a sentence.

> **Note:** Nested text uses SwiftUI's [Text concatenation](https://developer.apple.com/documentation/swiftui/text), so only modifiers that return `Text` (such as `bold`, `italic`, `font`, `foregroundColor`, and `foregroundStyle` with color) will apply to nested segments.

```tsx
import { Host, Text } from '@expo/ui/swift-ui';
import { bold, italic, foregroundStyle } from '@expo/ui/swift-ui/modifiers';

export default function NestedTextExample() {
  return (
    <Host matchContents>
      <Text>
        Hello <Text modifiers={[bold(), foregroundStyle('red')]}>world</Text>!
      </Text>
    </Host>
  );
}
```

### Mixed inline styles

Combine multiple styled segments for rich text formatting.

```tsx
import { Host, Text } from '@expo/ui/swift-ui';
import { bold, italic, foregroundStyle, font } from '@expo/ui/swift-ui/modifiers';

export default function MixedStylesExample() {
  return (
    <Host matchContents>
      <Text>
        This is <Text modifiers={[bold()]}>bold</Text>, <Text modifiers={[italic()]}>italic</Text>,
        and <Text modifiers={[foregroundStyle('orange')]}>colored</Text> text.
      </Text>
    </Host>
  );
}
```

### Font weights

Use the `font` modifier to apply different font weights.

```tsx
import { Host, Text, VStack } from '@expo/ui/swift-ui';
import { font } from '@expo/ui/swift-ui/modifiers';

export default function FontWeightsExample() {
  return (
    <Host matchContents>
      <VStack spacing={4}>
        <Text modifiers={[font({ weight: 'ultraLight' })]}>Ultra Light</Text>
        <Text modifiers={[font({ weight: 'light' })]}>Light</Text>
        <Text modifiers={[font({ weight: 'regular' })]}>Regular</Text>
        <Text modifiers={[font({ weight: 'medium' })]}>Medium</Text>
        <Text modifiers={[font({ weight: 'semibold' })]}>Semibold</Text>
        <Text modifiers={[font({ weight: 'bold' })]}>Bold</Text>
        <Text modifiers={[font({ weight: 'heavy' })]}>Heavy</Text>
        <Text modifiers={[font({ weight: 'black' })]}>Black</Text>
      </VStack>
    </Host>
  );
}
```

### Font designs

Use the `font` modifier to apply different font designs.

```tsx
import { Host, Text, VStack } from '@expo/ui/swift-ui';
import { font } from '@expo/ui/swift-ui/modifiers';

export default function FontDesignsExample() {
  return (
    <Host matchContents>
      <VStack spacing={4}>
        <Text modifiers={[font({ design: 'default', size: 18 })]}>Default Design</Text>
        <Text modifiers={[font({ design: 'rounded', size: 18 })]}>Rounded Design</Text>
        <Text modifiers={[font({ design: 'serif', size: 18 })]}>Serif Design</Text>
        <Text modifiers={[font({ design: 'monospaced', size: 18 })]}>Monospaced Design</Text>
      </VStack>
    </Host>
  );
}
```

### Custom fonts

Use the `font` modifier with a `family` parameter to use custom fonts. You can load custom fonts using [`expo-font`](/versions/latest/sdk/font.md) library.

```tsx
import { Host, Text, VStack } from '@expo/ui/swift-ui';
import { font } from '@expo/ui/swift-ui/modifiers';

export default function CustomFontExample() {
  return (
    <Host matchContents>
      <VStack spacing={4}>
        <Text modifiers={[font({ family: 'Inter-Bold', size: 18 })]}>Inter Bold</Text>
        <Text modifiers={[font({ family: 'Inter-Regular', size: 18 })]}>Inter Regular</Text>
      </VStack>
    </Host>
  );
}
```

### Text with line limit

Use the `lineLimit` modifier to truncate text after a certain number of lines.

```tsx
import { Host, Text } from '@expo/ui/swift-ui';
import { lineLimit } from '@expo/ui/swift-ui/modifiers';

export default function LineLimitExample() {
  const longText = 'This is a very long text that will be truncated after two lines. '.repeat(5);

  return (
    <Host matchContents>
      <Text modifiers={[lineLimit(2)]}>{longText}</Text>
    </Host>
  );
}
```

### Markdown

Use the `markdownEnabled` property to enable Markdown formatting for the text content.

```tsx
import { Host, Text, VStack } from '@expo/ui/swift-ui';

export default function MarkdownTextExample() {
  return (
    <Host matchContents>
      <VStack spacing={4}>
        <Text markdownEnabled>Regular text.</Text>
        <Text markdownEnabled>
          This is **bold text**, *italic text* and ***text in both bold and italic***.
        </Text>
        <Text markdownEnabled>~~Strikethrough text~~</Text>
        <Text markdownEnabled>`This is monospaced text`</Text>
        <Text markdownEnabled>
          Visit the [Expo Docs](https://docs.expo.dev/versions/latest/sdk/ui/) to learn more about
          Expo UI
        </Text>
      </VStack>
    </Host>
  );
}
```

### Auto-updating date

Use the `date` and `dateStyle` props to display a date that automatically updates as time passes. This is especially useful in widgets and Live Activities.

```tsx
import { Host, Text } from '@expo/ui/swift-ui';

export default function DateTextExample() {
  return (
    <Host matchContents>
      <Text date={new Date(Date.now() + 300000)} dateStyle="timer" />
    </Host>
  );
}
```

### Timer interval

Use `timerInterval` to display a live countdown or count-up timer. This requires iOS/tvOS 16+.

```tsx
import { Host, Text } from '@expo/ui/swift-ui';

export default function TimerIntervalExample() {
  return (
    <Host matchContents>
      <Text
        timerInterval={{ lower: new Date(), upper: new Date(Date.now() + 600000) }}
        countsDown
      />
    </Host>
  );
}
```

> **Note:** `timerInterval`, `countsDown`, and `pauseTime` require iOS 16.0+ / tvOS 16.0+. On older versions, the timer interval will not render.

## API

```tsx
import { Text } from '@expo/ui/swift-ui';
```

## Component

### `Text`

Supported platforms: iOS, tvOS.

Type: React.Element<[TextProps](https://reactnative.dev/docs/text#props)\>

TextProps

### `children`

Supported platforms: iOS, tvOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Text content or nested Text components.

### `countsDown`

Supported platforms: iOS 16.0+, tvOS 16.0+.

Optional • Type: `boolean` • Default: `true`

Whether the timer counts down (`true`) or up (`false`).

### `date`

Supported platforms: iOS, tvOS.

Optional • Type: [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)

A date to display using the specified `dateStyle`. The text auto-updates as time passes.

### `dateStyle`

Supported platforms: iOS, tvOS.

Optional • Type: [TextDateStyle](#textdatestyle) • Default: `'date'`

The style used to format the `date` prop.

### `markdownEnabled`

Supported platforms: iOS, tvOS.

Optional • Type: `boolean`

Enables Markdown formatting for the text content using SwiftUI LocalizedStringKey.

### `pauseTime`

Supported platforms: iOS 16.0+, tvOS 16.0+.

Optional • Type: [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)

A date at which the timer should appear paused.

### `timerInterval`

Supported platforms: iOS 16.0+, tvOS 16.0+.

Optional • Type: [ClosedRangeDate](#closedrangedate)

A time interval to display as a live-updating timer.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)

## Types

### `TextDateStyle`

Supported platforms: iOS, tvOS.

Literal Type: `string`

The style used to format a date in a SwiftUI `Text` view.

Acceptable values are: `'timer'` | `'relative'` | `'offset'` | `'date'` | `'time'`
