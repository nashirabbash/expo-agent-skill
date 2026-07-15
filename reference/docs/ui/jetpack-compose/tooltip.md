---
title: "Tooltip"
description: "Jetpack Compose Tooltip components for displaying contextual information on long-press."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/tooltip.md"
scraped_at: "2026-07-15T09:00:38.513612"
---

---
title: Tooltip
description: Jetpack Compose Tooltip components for displaying contextual information on long-press.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Tooltip

Jetpack Compose Tooltip components for displaying contextual information on long-press.
Android, Included in Expo Go

Expo UI Tooltip matches the official Jetpack Compose [Tooltip](https://developer.android.com/develop/ui/compose/components/tooltip) API. `TooltipBox` wraps anchor content and displays a tooltip. The tooltip content is provided via the `TooltipBox.PlainTooltip` or `TooltipBox.RichTooltip` compound components, which match [`PlainTooltip`](https://developer.android.com/develop/ui/compose/components/tooltip#display-plain) and [`RichTooltip`](https://developer.android.com/develop/ui/compose/components/tooltip#display-rich) respectively. Tooltips can be triggered by long-press or shown programmatically via `ref`.

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

### Plain tooltip

Long-press the anchor content to display the tooltip.

```tsx
import { Host, TooltipBox, Button, Text } from '@expo/ui/jetpack-compose';

export default function PlainTooltipExample() {
  return (
    <Host matchContents>
      <TooltipBox>
        <TooltipBox.PlainTooltip>
          <Text>Add to favorites</Text>
        </TooltipBox.PlainTooltip>
        <Button onClick={() => {}}>
          <Text>Favorite</Text>
        </Button>
      </TooltipBox>
    </Host>
  );
}
```

### Rich tooltip with title and body

Use `TooltipBox.RichTooltip` with `Title` and `Text` compound component pattern for more detailed contextual information.

```tsx
import { Host, TooltipBox, Button, Text } from '@expo/ui/jetpack-compose';

export default function RichTooltipExample() {
  return (
    <Host matchContents>
      <TooltipBox>
        <TooltipBox.RichTooltip>
          <TooltipBox.RichTooltip.Title>
            <Text>Camera</Text>
          </TooltipBox.RichTooltip.Title>
          <TooltipBox.RichTooltip.Text>
            <Text>Take photos and record videos with your device camera.</Text>
          </TooltipBox.RichTooltip.Text>
        </TooltipBox.RichTooltip>
        <Button onClick={() => {}}>
          <Text>Open Camera</Text>
        </Button>
      </TooltipBox>
    </Host>
  );
}
```

### Rich tooltip with action

Add an interactive action with `TooltipBox.RichTooltip.Action`. Use `isPersistent` so the tooltip stays visible for the user to tap it. `hasAction` is automatically derived when an action slot is present.

```tsx
import { Host, TooltipBox, Button, TextButton, Text } from '@expo/ui/jetpack-compose';

export default function RichTooltipActionExample() {
  return (
    <Host matchContents>
      <TooltipBox isPersistent>
        <TooltipBox.RichTooltip>
          <TooltipBox.RichTooltip.Title>
            <Text>Permissions Required</Text>
          </TooltipBox.RichTooltip.Title>
          <TooltipBox.RichTooltip.Text>
            <Text>This feature requires camera and microphone access.</Text>
          </TooltipBox.RichTooltip.Text>
          <TooltipBox.RichTooltip.Action>
            <TextButton onClick={() => {}}>
              <Text>Learn More</Text>
            </TextButton>
          </TooltipBox.RichTooltip.Action>
        </TooltipBox.RichTooltip>
        <Button onClick={() => {}}>
          <Text>Record Video</Text>
        </Button>
      </TooltipBox>
    </Host>
  );
}
```

### Programmatic show and dismiss

Use a `ref` to imperatively `show()` or `dismiss()` the tooltip without requiring a long-press.

```tsx
import { useRef } from 'react';
import { Host, TooltipBox, type TooltipBoxRef, Button, Text, Row } from '@expo/ui/jetpack-compose';

export default function ProgrammaticTooltipExample() {
  const tooltipRef = useRef<TooltipBoxRef>(null);

  return (
    <Host matchContents>
      <TooltipBox ref={tooltipRef} isPersistent>
        <TooltipBox.PlainTooltip>
          <Text>Shown programmatically!</Text>
        </TooltipBox.PlainTooltip>
        <Button onClick={() => {}}>
          <Text>Anchor</Text>
        </Button>
      </TooltipBox>
      <Row horizontalArrangement={{ spacedBy: 8 }}>
        <Button onClick={() => tooltipRef.current?.show()}>
          <Text>Show</Text>
        </Button>
        <Button onClick={() => tooltipRef.current?.dismiss()}>
          <Text>Dismiss</Text>
        </Button>
      </Row>
    </Host>
  );
}
```

## API

```tsx
import { TooltipBox } from '@expo/ui/jetpack-compose';
```

## Component

### `TooltipBox`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[TooltipBoxProps](#tooltipboxprops)\>

A container that wraps anchor content and shows a tooltip on long-press. Provide the tooltip content via `TooltipBox.PlainTooltip` or `TooltipBox.RichTooltip`. All other children are the anchor/trigger.

Use `ref` to imperatively `show()` or `dismiss()` the tooltip.

TooltipBoxProps

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children containing a `TooltipBox.PlainTooltip` or `TooltipBox.RichTooltip` slot and the anchor/trigger content. The anchor content triggers the tooltip on long-press.

### `enableUserInput`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether user input (long-press, hover) triggers the tooltip.

### `focusable`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

Whether the tooltip popup is focusable.

### `hasAction`

Supported platforms: Android.

Optional • Type: `boolean`

Whether the tooltip contains an action. Affects accessibility and dismiss behavior. When not specified, this is automatically derived from the presence of a `RichTooltip.Action` slot.

### `isPersistent`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `false`

Whether the tooltip persists instead of auto-dismissing after a short timeout.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `ref`

Supported platforms: Android.

Optional • Type: Ref<[TooltipBoxRef](#tooltipboxref)\>

Ref to imperatively show/dismiss the tooltip.

## Types

### `TooltipBoxRef`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| dismiss | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Programmatically dismisses the tooltip. |
| show | () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\> | Programmatically shows the tooltip. |
